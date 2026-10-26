from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

OLLAMA_BASE_URL = os.environ.get('OLLAMA_BASE_URL', 'http://127.0.0.1:11434')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    payload = {
        "model": data.get("model", "qwen3:1.7b"),
        "messages": data.get("messages", []),
        "stream": data.get("stream", False)
    }
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/v1/chat/completions",
            json=payload,
            timeout=300
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Cannot connect to Ollama server. Is it running on port 11434?"}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/models', methods=['GET'])
def list_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=30)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Cannot connect to Ollama server. Is it running on port 11434?"}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "ollama": "connected"}), 200

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
