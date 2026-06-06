from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import whisper
import ollama
import edge_tts
import asyncio
import uuid

app = Flask(__name__)
CORS(app)

# LOAD WHISPER MODEL
whisper_model = whisper.load_model("base")

# THERAPIST AI PROMPT
SYSTEM_PROMPT = """
You are a professional AI therapist.
Speak calmly, empathetically, and professionally.
Provide emotional support and reflective questions.
Avoid overly personal language.
Do not diagnose medical conditions.
"""

# VOICE CHAT API
@app.route("/voice-chat", methods=["POST"])
def voice_chat():

    # RECEIVE AUDIO
    audio = request.files["audio"]

    # SAVE AUDIO
    input_filename = f"{uuid.uuid4()}.webm"

    audio.save(input_filename)

    # SPEECH TO TEXT
    result = whisper_model.transcribe(input_filename)

    user_text = result["text"]

    print("USER SAID:", user_text)

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

    print("AI REPLY:", ai_reply)

    # GENERATE UNIQUE AUDIO FILE
    output_mp3 = f"{uuid.uuid4()}.mp3"

    # TEXT TO SPEECH
    async def generate_voice():

        communicate = edge_tts.Communicate(
            ai_reply,
            voice="en-US-AriaNeural"
        )

        await communicate.save(output_mp3)

        print("VOICE FILE CREATED:", output_mp3)

    asyncio.run(generate_voice())

    # RETURN RESPONSE
    return jsonify({
        "user_text": user_text,
        "ai_reply": ai_reply,
        "voice_file": output_mp3
    })

# SERVE AUDIO FILE
@app.route("/audio/<filename>")
def serve_audio(filename):

    return send_file(
        filename,
        mimetype="audio/mpeg"
    )

# START SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)