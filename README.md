# MindMate – Mental Health Chatbot

## **Project Aim**
MindMate is an AI-powered mental health chatbot that analyzes user mood based on text input and provides suggestions and tips to improve mental well-being.

---

## **Features**
- Analyze user mood: Positive, Negative, or Neutral
- Provide suggestions for coping with mood
- Maintain chat history with timestamps
- Offer extra tips for mental health improvement
- Example outputs displayed directly in the README for easy reference

---

## **How to Run Locally**

1. **Clone the repository**
```bash
git clone https://github.com/KakanuruPrathibhaReddy/MindMate.git
cd MindMate
```

2. **Create and activate a virtual environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the FastAPI app**
```bash
uvicorn main:app --reload
```

5. **Open the app**
- Visit `http://127.0.0.1:8000` in your browser
- You can access endpoints like `/analyze` (POST) and `/history` (GET)

## **Sample API Output**

### **1. Analyze Mood Example**

**Input:**  
```
I am feeling very happy today!
```

**Output:**  
```json
{
  "mood": "Positive",
  "suggestion": "Great! Keep doing things that make you happy.",
  "extra_tips": [
    "Keep smiling and stay optimistic.",
    "Share your happiness with friends or family.",
    "Take time to enjoy your favorite hobbies."
  ]
}

**Input:**  
```
I feel sad and stressed with everything.
```

**Output:**  
```json
{
  "mood": "Negative",
  "suggestion": "It’s okay to feel low. Try talking to a friend or journaling.",
  "extra_tips": [
    "Take deep breaths to relax.",
    "Go for a short walk or stretch.",
    "Listen to calming music or meditate."
  ]
}
**Input:**  
```
I am just okay, nothing special today.
```

**Output:**  
```json
{
  "mood": "Neutral",
  "suggestion": "Your mood seems balanced. Try a relaxing activity like reading.",
  "extra_tips": [
    "Maintain your daily routine for stability.",
    "Take short breaks to recharge.",
    "Engage in a small hobby to lift your mood."
  ]
}
### **2. Chat History Example**

```json
[
  {
    "timestamp": "2025-08-24 11:50:00",
    "text": "I am feeling very happy today!",
    "mood": "Positive",
    "suggestion": "Great! Keep doing things that make you happy."
  },
  {
    "timestamp": "2025-08-24 12:05:00",
    "text": "I feel sad and stressed with everything.",
    "mood": "Negative",
    "suggestion": "It’s okay to feel low. Try talking to a friend or journaling."
  },
  {
    "timestamp": "2025-08-24 12:20:00",
    "text": "I am just okay, nothing special today.",
    "mood": "Neutral",
    "suggestion": "Your mood seems balanced. Try a relaxing activity like reading."
  }
]
## **Notes**
- This project uses **FastAPI** for backend.  
- **VADER Sentiment Analyzer** is used for mood detection.  
- `.gitignore` is configured to ignore unnecessary files like `__pycache__` and the virtual environment `.venv`.  
- All outputs are shown in this README for easy review without running the code. 
