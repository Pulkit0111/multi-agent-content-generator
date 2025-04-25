import os
from dotenv import load_dotenv
from agents import research_agent, writer_agent, editor_agent

load_dotenv()

def run_pipeline(topic):
    print(f"\n📌 Running Multi-agent content pipeline for: {topic}\n")
    #step 1: research
    research_summary = research_agent(topic)
    #step 2: write
    draft_article = writer_agent(research_summary)
    #step 3: edit
    polished_article = editor_agent(draft_article)
    
    return polished_article
    
if __name__ == "__main__":
    topic = input("Enter a topic to generate the article: ")
    article = run_pipeline(topic)
    print("\n📝 Final Article:")
    print(article)
