# from flask import Flask, request, jsonify
# import speech_recognition as sr
# from io import BytesIO

# app = Flask(__name__)

# @app.route('/speech-to-text', methods=['POST'])
# def speech_to_text():
#     try:
#         # Receive the audio file from the frontend
#         audio_file = request.files['audio']
#         recognizer = sr.Recognizer()
        
#         # Process the audio file
#         audio_data = sr.AudioFile(BytesIO(audio_file.read()))
#         with audio_data as source:
#             audio = recognizer.record(source)
#         text = recognizer.recognize_google(audio)  # Convert speech to text
        
#         return jsonify({'text': text})  # Return the text response
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import speech_recognition as sr
from io import BytesIO
import os

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
    port = int(os.environ.get("PORT", 5000))  # Get port from environment variable
    app.run(host='0.0.0.0', port=port, debug=False)  # Set host to 0.0.0.0
