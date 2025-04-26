import os
from dotenv import load_dotenv
from agents import research_agent, writer_agent, editor_agent
from rich import print
import argparse
load_dotenv()

def save_to_markdown(content, topic):
    filename = f"{topic.lower().replace(' ', '_')}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\n📝 [bold green]Article saved to[/bold green] [yellow]{filename}[/yellow]")
    
def run_pipeline(topic):
    print(f"\n📌 [bold green]Running Content Generation Pipeline[/bold green] for: [yellow]{topic}[/yellow]")
    #step 1: research
    research_summary = research_agent(topic)
    #step 2: write
    draft_article = writer_agent(research_summary)
    #step 3: edit
    polished_article = editor_agent(draft_article, research_summary)
    save_to_markdown(polished_article, topic)

def main():
    parser = argparse.ArgumentParser(
        description="Multi-Agent Content Generator CLI"
    )
    parser.add_argument(
        "--topic", type=str, required=True, 
        help="Topic to generate content for."
    )
    
    args = parser.parse_args()

    run_pipeline(args.topic)

if __name__ == "__main__":
    main()

