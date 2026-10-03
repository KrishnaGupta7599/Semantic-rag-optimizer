from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Question(BaseModel):
    question:str

@app.get("/")
def home():
    return {"message":"Semantic RAG Optimiser is running"}

@app.post("/ask")
def ask(question:Question):
    return {"you_asked": question.question}