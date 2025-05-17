
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app, origins="*", supports_credentials=True)

@app.route("/api/emotion_logs")
def emotion_logs():
    return jsonify([
        {"date": "2025-05-10", "emotion": "Anxiety", "intensity": 6},
        {"date": "2025-05-11", "emotion": "Stress", "intensity": 7},
        {"date": "2025-05-12", "emotion": "Calm", "intensity": 3}
    ])

@app.route("/api/analyze_journal", methods=["POST"])
def analyze_journal():
    entry = request.json.get("entry", "")
    return jsonify({
        "emotion_tone": "Neutral",
        "summary": [
            "Client expressed uncertainty about a decision.",
            "Theme of fear and desire for clarity."
        ],
        "follow_ups": [
            "What would feeling confident look like?",
            "When have you handled something like this before?"
        ]
    })

@app.route("/api/recommend_coping", methods=["POST"])
def recommend_coping():
    emotion = request.json.get("emotion", "").lower()
    suggestions = {
        "anxiety": ["Deep breathing", "Grounding techniques", "Talking to a friend"],
        "sadness": ["Walk in nature", "Journaling", "Listening to music"],
        "anger": ["Box breathing", "Taking a timeout", "Expressive writing"]
    }
    return jsonify({
        "emotion": emotion,
        "recommendations": suggestions.get(emotion, ["Take a break", "Drink water", "Step away briefly"])
    })

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
