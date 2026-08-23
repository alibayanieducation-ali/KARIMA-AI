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