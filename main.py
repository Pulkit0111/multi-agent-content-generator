import os
from dotenv import load_dotenv
from agents import research_agent, writer_agent, editor_agent
import argparse
load_dotenv()

def save_to_markdown(content, topic):
    filename = f"{topic.lower().replace(' ', '_')}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\n📝 Article saved to {filename}")
    
def run_pipeline(topic):
    print(f"\n📌 Running Multi-agent content pipeline for: {topic}\n")
    #step 1: research
    research_summary = research_agent(topic)
    #step 2: write
    draft_article = writer_agent(research_summary)
    #step 3: edit
    polished_article = editor_agent(draft_article, research_summary)
    save_to_markdown(polished_article, topic)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", help="Topic to generate article for")
    args = parser.parse_args()

    if args.topic:
        run_pipeline(args.topic)
    else:
        topic = input("Enter a topic to generate content: ")
        run_pipeline(topic)

