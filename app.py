from flask import Flask, request, jsonify
import whisper
import ollama
import edge_tts
import asyncio
import uuid

app = Flask(__name__)

# LOAD WHISPER MODEL
whisper_model = whisper.load_model("base")

# THERAPIST PERSONALITY
SYSTEM_PROMPT = """
You are a professional AI therapist.
Speak calmly, empathetically, and professionally.
Provide emotional support and reflective questions.
Avoid overly personal language.
Do not diagnose medical conditions.
"""

# TEXT CHAT API
@app.route("/ai-chat", methods=["POST"])
def ai_chat():

    data = request.json

    user_message = data["message"]

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_reply = response["message"]["content"]

    return jsonify({
        "reply": ai_reply
    })

# VOICE CHAT API
@app.route("/voice-chat", methods=["POST"])
def voice_chat():

    audio = request.files["audio"]

    filename = f"{uuid.uuid4()}.wav"

    audio.save(filename)

    # SPEECH TO TEXT
    result = whisper_model.transcribe(filename)

    user_text = result["text"]

    # AI RESPONSE
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    ai_reply = response["message"]["content"]

    # TEXT TO SPEECH
    async def generate_voice():

        communicate = edge_tts.Communicate(
            ai_reply,
            voice="en-US-AriaNeural"
        )

        await communicate.save("response.mp3")

    asyncio.run(generate_voice())

    return jsonify({
        "user_text": user_text,
        "ai_reply": ai_reply,
        "voice_file": "response.mp3"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)