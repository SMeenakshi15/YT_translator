# # Import necessary libraries
# import googletrans  # For language translation
# from textblob import TextBlob  # For language detection and translation

# # Create a Translator object from the googletrans library
# translator = googletrans.Translator()

# # Open a file for writing the translated text (replace with your desired file path)
# t = open("translated_file.txt", "w", encoding="utf-8")

# # Open the transcript file for reading (replace with your transcript file path)
# with open("transcript_file.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         # Detect the language of the current line in the transcript
#         lang = translator.detect(line)

#         # Print the detected language for the current line
#         print("Language detected: ", lang)

#         # Translate the current line to the destination language ('hi' for Hindi in this case)
#         translated = translator.translate(line, dest='hi')

#         # Get the translated text from the translation object
#         txt = translated.text

#         # Write the translated text to the output file
#         t.write(txt)

# # Close the input and output files
# f.close()
# t.close()


# Import necessary libraries
import googletrans  # For language translation

# Create a Translator object from the googletrans library
translator = googletrans.Translator()

# Open the transcript file for reading
with open("transcript_file.txt", "r", encoding="utf-8") as f:
    # Read the entire content of the transcript
    transcript_text = f.read()

# Translate the transcript to the destination language ('hi' for Hindi in this case)
translated = translator.translate(transcript_text, dest='hi')

# Get the translated text from the translation object
translated_text = translated.text

# Open a file for writing the translated text
with open("translated_file.txt", "w", encoding="utf-8") as t:
    t.write(translated_text)
