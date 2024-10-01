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


import streamlit as st
import speech_recognition as sr
from io import BytesIO

# Function to handle speech-to-text conversion
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    try:
        # Process the audio file using SpeechRecognition
        audio_data = sr.AudioFile(BytesIO(audio_file.read()))
        with audio_data as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)  # Convert speech to text
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app interface
st.title("Speech to Text Converter")

# File uploader for the audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    st.write("Processing audio file...")
    # Convert the uploaded audio to text
    text = speech_to_text(uploaded_file)
    st.write("Converted Text:")
    st.write(text)
