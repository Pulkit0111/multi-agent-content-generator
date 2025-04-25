import os
from dotenv import load_dotenv
from agents import research_agent, writer_agent, editor_agent

load_dotenv()

def main():
    topic = "The latest trends in Artificial Intelligence"
    research_summary = research_agent(topic)
    draft_article = writer_agent(research_summary)
    polished_article = editor_agent(draft_article)
    print("\nFinal Article:")  
    print(polished_article)
    
    
if __name__ == "__main__":
    main()