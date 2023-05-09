import os

from flask import Flask
from langchain.llms import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    llm = OpenAI(temperature=0.9)
    text = "What is a project good for ?"

    return text, llm(text)
