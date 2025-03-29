from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mixtral-8x7b-instruct"  # You can change to gpt-4, llama-3, etc.

@app.route('/')
def home():
    return "✅ AI Agent Backend (OpenRouter) is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "No input provided"}), 400

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": message}]
            }
        )
        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            return jsonify({"reply": reply})
        else:
            return jsonify({"reply": "Error from OpenRouter", "details": response.text}), 500

    except Exception as e:
        return jsonify({"reply": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
