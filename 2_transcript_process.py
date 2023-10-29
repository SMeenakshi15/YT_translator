# Import the necessary libraries
import speech_recognition as sr  # For speech recognition

# Create a Recognizer object from the SpeechRecognition library
r = sr.Recognizer()

# Open the audio file for recognition (replace with the actual file path)
audio_path = "extracted_audio(2).wav"  # Assuming the audio file is in the same directory
with sr.AudioFile(audio_path) as source:
    # Adjust for ambient noise to improve recognition accuracy
    r.adjust_for_ambient_noise(source)
    # Record audio from the source file for a specified duration (20 seconds in this case)
    audio = r.record(source, duration=20)

# Recognize the speech in the audio using Google Web Speech API and specify the target language as 'en-UK' (British English)
text = r.recognize_google(audio, language='en-UK')

# Print the recognized text
print(text)

# Open a file for writing the transcript
with open("transcript_file.txt", "w") as f:  # Make sure to change the file extension to '.txt'
    # Write the entire recognized text to the file
    f.write(text)
