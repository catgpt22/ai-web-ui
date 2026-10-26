from flask import Flask, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__)

OLLAMA_BASE_URL = os.environ.get('OLLAMA_BASE_URL', 'http://127.0.0.1:11434')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/v1/chat/completions",
            json=data,
            timeout=300
        )
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/models', methods=['GET'])
def list_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return {"status": "ok", "ollama": "connected"}

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
