from flask import Flask, request, jsonify
import speech_recognition as sr
from io import BytesIO

app = Flask(__name__)

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    try:
        # Receive the audio file from the frontend
        audio_file = request.files['audio']
        recognizer = sr.Recognizer()
        
        # Process the audio file
        audio_data = sr.AudioFile(BytesIO(audio_file.read()))
        with audio_data as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)  # Convert speech to text
        
        return jsonify({'text': text})  # Return the text response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)