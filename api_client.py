import os
from dotenv import load_dotenv
from openai import OpenAI
from tavily import TavilyClient

load_dotenv()

gpt_client = OpenAI(api_key=os.getenv("GPT_API_KEY")) 

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

MODEL = "gpt-4o-mini"