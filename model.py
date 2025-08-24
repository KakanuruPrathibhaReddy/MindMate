from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

analyzer = SentimentIntensityAnalyzer()
chat_history = []

# Extra tips for each mood
mood_tips = {
    "Positive": [
        "Keep up the positive mindset!",
        "Share your happiness with others.",
        "Keep doing things that make you feel good."
    ],
    "Negative": [
        "Take a short walk to clear your mind.",
        "Talk to a friend or family member about your feelings.",
        "Try journaling to express your thoughts."
    ],
    "Neutral": [
        "Maintain your balance with meditation or deep breathing.",
        "Engage in a relaxing hobby.",
        "Reflect on what made your day balanced today."
    ]
}

def analyze_mood(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        mood = "Positive"
        suggestion = "Great! Keep doing things that make you happy."
    elif compound <= -0.05:
        mood = "Negative"
        suggestion = "It’s okay to feel low. Try talking to a friend or journaling."
    else:
        mood = "Neutral"
        suggestion = "Your mood seems balanced. Try a relaxing activity like reading."

    # Add extra tips based on mood
    tips = mood_tips[mood]

    chat_history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        "mood": mood,
        "suggestion": suggestion,
        "tips": tips
    })

    return {"mood": mood, "suggestion": suggestion, "tips": tips}

def get_chat_history():
    return chat_history
