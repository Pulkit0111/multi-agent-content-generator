import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("GPT_API_KEY")) 

MODEL = "gpt-3.5-turbo"