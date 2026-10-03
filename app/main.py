import os

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app=FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Question(BaseModel):
    question:str

@app.get("/")
def home():
    return {"message":"Semantic RAG Optimiser is running"}

@app.post("/ask")
def ask(question:Question):
    response = client.chat.completions.create(
       model="openai/gpt-oss-120b",
         messages=[
            {
                "role": "user",
                "content": question.question
            }
        ]
    )
    answer = response.choices[0].message.content

    return {"answer": answer}