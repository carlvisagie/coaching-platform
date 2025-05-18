from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True)

@app.route("/api/emotion_logs")
def emotion_logs():
    return jsonify([
        {"date": "2025-05-10", "emotion": "Anxiety", "intensity": 6},
        {"date": "2025-05-11", "emotion": "Stress", "intensity": 7},
        {"date": "2025-05-12", "emotion": "Calm", "intensity": 3}
    ])

# 🔥 EXPOSE FOR GUNICORN
gunicorn_app = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)



