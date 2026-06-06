# AI Therapist Service

## Features

* Therapist-style AI conversation
* Speech-to-text using Whisper
* AI responses using Llama3
* Text-to-speech voice output
* Flask API backend
* Flutter-app compatible

---

# Setup Instructions

## 1. Install Python

Download Python from:
https://www.python.org/downloads/

---

## 2. Install Ollama

Download Ollama from:
https://ollama.com/download/windows

---

## 3. Install Llama3 Model

Run:

```bash
ollama run llama3
```

---

## 4. Install Python Dependencies

Inside project folder run:

```bash
pip install -r requirements.txt
```

---

## 5. Run Backend Server

```bash
python app.py
```

Server runs at:

```text
http://127.0.0.1:5000
```

---

# API Endpoints

## Text Chat Endpoint

POST:

```text
/ai-chat
```

JSON:

```json
{
  "message": "I feel stressed lately"
}
```

---

## Voice Chat Endpoint

POST:

```text
/voice-chat
```

Form-data:

* audio file (.wav)

---

# Tech Stack

* Python
* Flask
* Ollama
* Llama3
* Whisper
* Edge-TTS
