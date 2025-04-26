from api_client import gpt_client, MODEL
from prompt_templates import RESEARCH_PROMPT_TEMPLATE, WRITER_PROMPT_TEMPLATE, EDITOR_PROMPT_TEMPLATE
from tools import web_Search_tool

def call_gpt(prompt):
    """
    Call the GPT model with the given model and messages
    """
    completion = gpt_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message.content

def research_agent(topic):
    """
    Research agent that gathers information on a given topic
    """
    print("\n🌐 Searching the web for information...")
    search_results = web_Search_tool(topic)
    prompt = RESEARCH_PROMPT_TEMPLATE.format(search_results=search_results)
    research_summary = call_gpt(prompt)
    return research_summary

def writer_agent(research_summary):
    """
    Writer agent that creates a draft article based on research
    """
    print("\n🖌️ Writing a draft article...")
    prompt = WRITER_PROMPT_TEMPLATE.format(research=research_summary)
    draft_article = call_gpt(prompt)
    return draft_article

def editor_agent(draft_article, research_summary):
    """
    Editor agent that polishes and improves the draft article
    """
    print("\n🔍 Reviewing and polishing the article...")
    prompt = EDITOR_PROMPT_TEMPLATE.format(draft=draft_article, research=research_summary)
    polished_article = call_gpt(prompt)
    return polished_article