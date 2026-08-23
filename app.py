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
import os
import json
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Karima:
    def __init__(self, name="Karima"):
        self.name = name
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.tasks = []
        self.notes = []
        self.conversation_history = []
        
    def greet(self) -> str:
        hour = datetime.now().hour
        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        return f"{greeting}! I'm {self.name}, your personal AI assistant. How can I help you today? 🌟"
    
    def chat(self, message: str) -> str:
        """Enhanced chat with context awareness"""
        # Add to history
        self.conversation_history.append({"role": "user", "content": message})
        
        # Check for task-related commands
        if "add task" in message.lower() or "todo" in message.lower():
            return self._handle_task_command(message)
        
        if "show tasks" in message.lower() or "list tasks" in message.lower():
            return self.list_tasks()
        
        if "note" in message.lower() or "remember" in message.lower():
            return self._handle_note_command(message)
        
        # Regular chat with context
        try:
            messages = [
                {"role": "system", "content": f"You are {self.name}, a friendly helpful assistant. You can help with tasks, notes, and general questions."},
            ] + self.conversation_history[-5:]  # Last 5 exchanges for context
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150
            )
            reply = response.choices[0].message["content"]
            self.conversation_history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"I'm having trouble connecting. Error: {str(e)}"
    
    def _handle_task_command(self, message: str) -> str:
        """Extract and add task from natural language"""
        # Simple extraction - improve with NLP later
        task_text = message.replace("add task", "").replace("todo", "").strip()
        if task_text:
            return self.add_task(task_text)
        return "What task would you like to add?"
    
    def _handle_note_command(self, message: str) -> str:
        """Extract and save note"""
        note_text = message.replace("note", "").replace("remember", "").strip()
        if note_text:
            return self.save_note(note_text)
        return "What would you like me to note?"
    
    def add_task(self, task: str, priority="medium") -> str:
        """Add a new task"""
        task_id = len(self.tasks) + 1
        self.tasks.append({
            "id": task_id,
            "task": task,
            "priority": priority,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "completed": False
        })
        self._save_data()
        return f"✅ Task added: '{task}' (Priority: {priority})"
    
    def list_tasks(self) -> str:
        """List all tasks"""
        if not self.tasks:
            return "🎉 No tasks! You're all caught up!"
        
        pending = [t for t in self.tasks if not t["completed"]]
        if not pending:
            return "🎉 All tasks completed! Great job!"
        
        task_list = "📋 Your tasks:\n"
        for t in pending:
            task_list += f"  {t['id']}. {t['task']} [Priority: {t['priority']}]\n"
        return task_list
    
    def complete_task(self, task_id: int) -> str:
        """Mark a task as complete"""
        for t in self.tasks:
            if t["id"] == task_id and not t["completed"]:
                t["completed"] = True
                self._save_data()
                return f"✅ Task '{t['task']}' completed! 🎉"
        return "Task not found or already completed."
    
    def save_note(self, content: str) -> str:
        """Save a note"""
        note = {
            "id": len(self.notes) + 1,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.notes.append(note)
        self._save_data()
        return f"📝 Note saved: '{content[:50]}...'"
    
    def _save_data(self):
        """Save tasks and notes to file"""
        data = {
            "tasks": self.tasks,
            "notes": self.notes
        }
        with open("karima_data.json", "w") as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load saved data"""
        try:
            with open("karima_data.json", "r") as f:
                data = json.load(f)
                self.tasks = data.get("tasks", [])
                self.notes = data.get("notes", [])
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    karima = Karima()
    karima.load_data()
    print(karima.greet())
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"{karima.name}: Goodbye! Have a great day! 👋")
            break
        
        reply = karima.chat(user_input)
        print(f"{karima.name}: {reply}")