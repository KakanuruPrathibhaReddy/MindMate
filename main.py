from fastapi import FastAPI
from pydantic import BaseModel
from model import analyze_mood, get_chat_history  # Import functions from model.py

app = FastAPI(
    title="MindMate Mental Health API",
    description="Analyze user mood and suggest coping strategies",
    version="1.0.0"
)

class UserInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to MindMate Mental Health Chatbot API"}

@app.post("/analyze")
def analyze(input_data: UserInput):
    return analyze_mood(input_data.text)

@app.get("/history")
def history():
    return {"history": get_chat_history()}

@app.get("/help")
def help_info():
    tips = [
        "Take regular breaks and stay hydrated.",
        "Practice deep breathing or meditation for stress relief.",
        "Reach out to loved ones when feeling low or anxious.",
        "Get enough sleep to maintain mental and emotional balance.",
        "Engage in light physical activity like walking or stretching.",
        "Maintain a balanced diet and avoid excessive caffeine or sugar.",
        "Set realistic daily goals and prioritize tasks to reduce overwhelm.",
        "Write down your thoughts and feelings in a journal.",
        "Listen to calming music or practice mindfulness exercises.",
        "Seek professional help if you feel persistently sad or stressed.",
        "Limit screen time, especially on social media, to reduce anxiety.",
        "Practice gratitude by noting 2–3 things you’re thankful for each day.",
        "Create a comfortable personal space to relax and recharge.",
        "Try hobbies or activities that make you happy.",
        "Stay socially connected through calls or safe meet-ups with friends.",
        "Take short nature breaks to refresh your mind."
    ]
    return {"tips": tips}
