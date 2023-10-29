# # Import the necessary libraries
# import speech_recognition as sr  # For speech recognition

# # Create a Recognizer object from the SpeechRecognition library
# r = sr.Recognizer()

# # Open the audio file for recognition (replace with the actual file path)
# audio_path = "extracted_audio(2).wav"  # Assuming the audio file is in the same directory
# with sr.AudioFile(audio_path) as source:
#     # Adjust for ambient noise to improve recognition accuracy
#     r.adjust_for_ambient_noise(source)
#     # Record audio from the source file for a specified duration (20 seconds in this case)
#     audio = r.record(source, duration=20)

# # Recognize the speech in the audio using Google Web Speech API and specify the target language as 'en-UK' (British English)
# text = r.recognize_google(audio, language='en-UK')

# # Print the recognized text
# print(text)

# # Open a file for writing the transcript
# with open("transcript_file.txt", "w") as f:  # Make sure to change the file extension to '.txt'
#     # Write the entire recognized text to the file
#     f.write(text)


# Import the necessary libraries
# Import the necessary libraries
import speech_recognition as sr
import sys

# Get the source language from the command-line argument
source_language = sys.argv[0]

# Create a Recognizer object from the SpeechRecognition library
r = sr.Recognizer()

# Open the audio file for recognition (replace with the actual file path)
audio_path = "extracted_audio(2).wav"  # Assuming the audio file is in the same directory
with sr.AudioFile(audio_path) as source:
    # Adjust for ambient noise to improve recognition accuracy
    r.adjust_for_ambient_noise(source)
    # Record audio from the source file (no duration specified)
    audio = r.record(source)

try:
    # Recognize the speech in the entire audio using Google Web Speech API and specify the source language
    text = r.recognize_google(audio, language=source_language)

    # Print the recognized text
    print(text)

    # Open a file for writing the transcript
    with open("transcript_file.txt", "w", encoding="utf-8") as f:  # Make sure to change the file extension to '.txt'
        # Write the entire recognized text to the file
        f.write(text)

except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

except Exception as e:
    print(f"An error occurred: {e}")
