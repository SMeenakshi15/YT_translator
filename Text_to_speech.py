# Import the necessary libraries
from gtts import gTTS  # gtts library for text-to-speech conversion
from playsound import playsound  # playsound library for playing audio

# Prompt the user to input the destination language and store it in the 'dest_lang' variable
dest_lang = input("Enter the language:")

# Define a function for converting text to speech
def text_to_speech(text, language=dest_lang, output_file='output.mp3'):
    # Create a gTTS (Google Text-to-Speech) object with the specified text and language
    tts = gTTS(text, lang=language)
    # Save the generated audio to an output file, which is 'output.mp3' by default
    tts.save(output_file)
    # Note: The 'playsound' function, which plays the audio, is currently commented out.

# Open a file named "translated_file" for reading with UTF-8 encoding
with open("translated_file", "r", encoding="utf-8") as f:
    # Iterate through each line in the file
    for line in f:
        text = line  # Store the current line of text in the 'text' variable

# Call the 'text_to_speech' function with the 'text' from the last line of the file
text_to_speech(text)
