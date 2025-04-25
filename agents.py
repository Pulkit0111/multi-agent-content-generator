from api_client import client, MODEL
from prompt_templates import RESEARCH_PROMPT_TEMPLATE, WRITER_PROMPT_TEMPLATE, EDITOR_PROMPT_TEMPLATE

def call_gpt(prompt):
    """
    Call the GPT model with the given model and messages
    """
    completion = client.chat.completions.create(
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
    prompt = RESEARCH_PROMPT_TEMPLATE.format(topic=topic)
    research_summary = call_gpt(prompt)
    return research_summary

def writer_agent(research_summary):
    """
    Writer agent that creates a draft article based on research
    """
    prompt = WRITER_PROMPT_TEMPLATE.format(research=research_summary)
    draft_article = call_gpt(prompt)
    return draft_article

def editor_agent(draft_article):
    """
    Editor agent that polishes and improves the draft article
    """
    prompt = EDITOR_PROMPT_TEMPLATE.format(draft=draft_article)
    polished_article = call_gpt(prompt)
    return polished_article