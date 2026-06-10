# AI Therapist Service

A simple AI Therapist prototype built using Flask, Ollama, and a local frontend setup.
The project explores voice-based AI interaction workflows including speech-to-text, AI-generated responses, and backend communication.

---

# Features

* Local AI chatbot setup
* Flask backend server
* Frontend hosted locally
* AI response generation using Ollama
* Basic voice interaction workflow
* API communication between frontend and backend

---

# Tech Stack

* Python
* Flask
* Ollama
* HTML/CSS/JavaScript
* Local HTTP Server

---

# Project Structure

```bash
AI-Therapist-Service/
│
├── app.py
├── index.html
├── static/
├── templates/
└── README.md
```

---

# Running the Project

## 1. Start Ollama

```bash
ollama serve
```

---

## 2. Run the AI Model

Example:

```bash
ollama run llama3
```

---

## 3. Start Frontend Server

```bash
python -m http.server 8000
```

Frontend runs on:

```text
http://localhost:8000
```

---

## 4. Start Flask Backend

```bash
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

---

# Workflow

```text
User Voice/Input
↓
Speech-to-Text
↓
AI Processing using Ollama
↓
Response Generation
↓
Voice/Text Output
```

---

# Purpose

This project was created to explore AI-powered conversational workflows and understand how voice interaction systems communicate between frontend interfaces, backend APIs, and local AI models.

---

# Notes

* This project runs locally for development/testing purposes.
* Ollama must be running before starting the backend server.
* Flask is used as a lightweight backend API server.
