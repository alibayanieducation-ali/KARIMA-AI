print("Hello! I am Karima, your personal AI assistant.")
print("How can I help you today?")
# app.py

class Karima:
    def __init__(self, name="Karima"):
        self.name = name

    def greet(self):
        return f"Hello! I’m {self.name}, your personal assistant."

    def answer_question(self, question: str) -> str:
        return f"You asked: '{question}'. I’ll learn to answer this better soon!"

    def help_with_task(self, task: str) -> str:
        return f"Let’s break down your task: {task}."

    def organize_info(self, info: str) -> str:
        return f"Here’s your organized info:\n- {info}"


if __name__ == "__main__":
    karima = Karima()
    print(karima.greet())
    print(karima.answer_question("What is photosynthesis?"))
    print(karima.help_with_task("Prepare a study plan"))
    print(karima.organize_info("Shopping list: apples, bread, milk"))
python app.py
Hello! I’m Karima, your personal assistant.
You asked: 'What is photosynthesis?'. I’ll learn to answer this better soon!
Let’s break down your task: Prepare a study plan.
Here’s your organized info:
- Shopping list: apples, bread, milk
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # بارگذاری کلید API از فایل .env

class Karima:
    def __init__(self, name="Karima"):
        self.name = name
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, message: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are {self.name}, a friendly helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message["content"]

if __name__ == "__main__":
    karima = Karima()
    print(karima.greet())
    user_input = input("You: ")
    reply = karima.chat(user_input)
    print(f"{karima.name}: {reply}")