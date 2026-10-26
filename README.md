# 🤖 Local AI Assistant (Jarvis)

Offline personal AI assistant for Ahmad.

## Features
- Fully offline local AI (no cloud dependencies)
- Qwen3-1.7B model (1.4 GB, fits in 3GB VRAM)
- Indonesian language support
- Web interface for chat

## Setup
1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull model: `ollama pull qwen3:1.7b`
3. Start AI service: `systemctl --user start ai-proyek`

## Web Interface
- Frontend: `index.html` (browser interface)
- Backend: `server.py` (Flask proxy for Ollama API)

## Access
- Local: `http://127.0.0.1:5000`
