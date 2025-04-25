from api_client import client, MODEL


def research_agent(topic):
    """
    Research agent that gathers information on a given topic
    """
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a research assistant. Provide a comprehensive summary of the given topic with key points and recent developments."},
            {"role": "user", "content": f"Research the following topic and provide a detailed summary: {topic}"}
        ]
    )
    
    return completion.choices[0].message.content

def writer_agent(research_summary):
    """
    Writer agent that creates a draft article based on research
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional content writer. Create a well-structured article based on the research provided."},
            {"role": "user", "content": f"Write an informative article based on this research:\n\n{research_summary}"}
        ]
    )
    
    return completion.choices[0].message.content

def editor_agent(draft_article):
    """
    Editor agent that polishes and improves the draft article
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert editor. Improve the writing quality, clarity, and structure of the given article without changing its core content."},
            {"role": "user", "content": f"Edit and polish the following article to make it more engaging and professional:\n\n{draft_article}"}
        ]
    )
    
    return completion.choices[0].message.content