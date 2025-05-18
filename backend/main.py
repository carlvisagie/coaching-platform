from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True)

# In-memory storage for journal entries
journal_entries = []

# Mock emotion-coping strategy mappings
coping_strategies = {
    "anxiety": ["Deep breathing", "Talk to someone", "Grounding exercises"],
    "stress": ["Progressive muscle relaxation", "Take a short walk", "Listen to calming music"],
    "anger": ["Count to 10", "Physical exercise", "Write down your thoughts"],
    "sadness": ["Connect with a friend", "Self-compassion practice", "Engage in a hobby"],
    "fear": ["Reality testing", "Visualization", "Small exposure steps"],
    "overwhelm": ["Break tasks into smaller steps", "Set boundaries", "Practice mindfulness"],
    "depression": ["Behavioral activation", "Seek professional help", "Maintain routine"],
    "frustration": ["Take a break", "Problem-solving exercise", "Express feelings constructively"],
    "calm": ["Gratitude practice", "Maintain healthy habits", "Journal positive experiences"],
    "joy": ["Savor the moment", "Share with others", "Creative expression"]
}

@app.route("/api/emotion_logs")
def emotion_logs():
    return jsonify([
        {"date": "2025-05-10", "emotion": "Anxiety", "intensity": 6},
        {"date": "2025-05-11", "emotion": "Stress", "intensity": 7},
        {"date": "2025-05-12", "emotion": "Calm", "intensity": 3}
    ])

@app.route("/api/analyze_journal", methods=["POST"])
def analyze_journal():
    """
    Analyze a journal entry and return insights
    
    Input: {"entry": "Journal text here"}
    Output: Emotion tone, summary points, and follow-up questions
    """
    data = request.get_json()
    entry = data.get("entry", "")
    
    # Mock analysis logic - in a real app, this would use NLP/AI
    emotion_tone = "Neutral"
    if "overwhelm" in entry.lower() or "stress" in entry.lower():
        emotion_tone = "Stressed"
    elif "happy" in entry.lower() or "joy" in entry.lower():
        emotion_tone = "Positive"
    elif "sad" in entry.lower() or "depress" in entry.lower():
        emotion_tone = "Negative"
    
    # Extract simple summary points
    words = entry.split()
    summary = []
    if "overwhelm" in entry.lower():
        summary.append("User felt overwhelmed")
    if "got through" in entry.lower() or "handle" in entry.lower():
        summary.append("Mention of coping strength")
    if len(summary) == 0:
        summary.append(f"Entry contains {len(words)} words")
    
    # Generate follow-up questions
    follow_ups = [
        "What helped you feel more in control?",
        "How do you typically handle overwhelm?"
    ]
    
    return jsonify({
        "emotion_tone": emotion_tone,
        "summary": summary,
        "follow_ups": follow_ups
    })

@app.route("/api/recommend_coping", methods=["POST"])
def recommend_coping():
    """
    Recommend coping strategies based on emotion
    
    Input: {"emotion": "anxiety"}
    Output: Emotion and list of coping recommendations
    """
    data = request.get_json()
    emotion = data.get("emotion", "").lower()
    
    # Get recommendations from our mapping or provide general ones
    recommendations = coping_strategies.get(emotion, [
        "Practice mindfulness",
        "Talk to someone you trust",
        "Take care of your physical needs"
    ])
    
    return jsonify({
        "emotion": emotion,
        "recommendations": recommendations
    })

@app.route("/api/journal_entries", methods=["POST"])
def add_journal_entry():
    """
    Add a new journal entry
    
    Input: {
        "date": "2025-05-18",
        "entry": "Journal text here",
        "emotion": "calm"
    }
    Output: Success confirmation with timestamp
    """
    data = request.get_json()
    
    # Validate required fields
    required_fields = ["date", "entry", "emotion"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    # Add timestamp to the entry
    entry = {
        "date": data["date"],
        "entry": data["entry"],
        "emotion": data["emotion"],
        "timestamp": datetime.now().isoformat()
    }
    
    # Store in our in-memory list
    journal_entries.append(entry)
    
    return jsonify({
        "success": True,
        "message": "Journal entry saved",
        "timestamp": entry["timestamp"]
    })

# 🔥 EXPOSE FOR GUNICORN
gunicorn_app = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)



