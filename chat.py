import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY is missing from your .env file.")

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.7,
)

response = model.invoke("Hi! Introduce yourself briefly.")
print(response.content)