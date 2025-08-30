from asyncio.streams import FlowControlMixin
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
import ollama


OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2:latest"


messages = [
    {"role": "user", "content": "provide the details of how to become a Chartered Accountent, can you provide the response in the structured approach with proper heading and bullet points"}
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False
}
ollama_response = ollama.chat(model=MODEL, messages=messages)

# response = requests.post(OLLAMA_API, headers=HEADERS, json=payload)
# print(response.json()["message"]["content"])

print(ollama_response)


#function to get API key for OpenAI from .env file
