import streamlit as st
import subprocess
import os

# Streamlit app title
st.title("YouTube Video Translator")

# Input for YouTube video URL
video_url = st.text_input("Enter the YouTube video URL:")

# Input for source language
source_language = st.text_input("Enter the source language (e.g., en for English):")

# Input for destination language
destination_language = st.text_input("Enter the destination language (e.g., hi for Hindi):")

# Define a temporary folder to store intermediate files
temp_folder = "temp_folder"

# Define a function to execute a subprocess command and capture its output
def run_subprocess(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out, err

# Create a function to integrate all backend modules
def translate_video(video_url, source_language, destination_language):
    # Step 1: Download YouTube video and extract audio to a temporary folder
    st.write("Step 1: Downloading the YouTube video and extracting audio...")
    download_command = f"python 1_yt_to_wav.py {video_url}"  # Pass the video_url as an argument
    out, err = run_subprocess(download_command)
    
    # Step 2: Transcribe the audio and save the transcript to a file
    st.write("Step 2: Transcribing the audio...")
    transcription_command = f"python 2_transcript_process.py {temp_folder}/extracted_audio.wav"
    out, err = run_subprocess(transcription_command)

    # Step 3: Translate the transcript and save it to a file
    st.write("Step 3: Translating the transcript...")
    translation_command = f"python 3_translate_process.py {temp_folder}/transcript.txt {source_language} {destination_language}"
    out, err = run_subprocess(translation_command)

    # Step 4: Convert the translated transcript to speech
    st.write("Step 4: Converting the transcript to speech...")
    tts_command = f"python Text_to_speech.py {destination_language}"
    out, err = run_subprocess(tts_command)

    # Return the file path to the generated audio
    return "output.mp3"

# Define a placeholder for the audio file path
audio_file_path = None

# Check if the user clicked the "Convert" button
if st.button("Convert"):
    if video_url and source_language and destination_language:
        # Create a temporary folder if it doesn't exist
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # Translate the video
        audio_file_path = translate_video(video_url, source_language, destination_language)

# Display the translated transcript
if audio_file_path:
    st.header("Translated Transcript:")
    st.audio(audio_file_path)

    # Provide a download link for the audio
    st.markdown(f'<a href="{audio_file_path}" download="translated_audio.mp3">Download Audio</a>', unsafe_allow_html=True)
