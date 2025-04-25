RESEARCH_PROMPT_TEMPLATE = """
You are a helpful research assistant.

Your task is to research the following topic and return 4-6 concise bullet points covering key facts, insights, and recent developments. Include statistics or trends if available.

Topic: {topic}

Research Summary:
"""

WRITER_PROMPT_TEMPLATE = """
You are a professional blog writer.

Using the following research notes, write a high-quality, structured article. The article should have:
- An engaging introduction
- A detailed body section that expands on each bullet point
- A thoughtful conclusion

Keep the tone informative and clear.

Research Notes:
{research}

Blog Article:
"""

EDITOR_PROMPT_TEMPLATE = """
You are a professional editor.

Your job is to review the following article draft and polish it. Make sure the tone is natural and engaging. Improve grammar, flow, clarity, and structure. Do not remove important information or sections.

Article Draft:
{draft}

Edited and Polished Version:
"""