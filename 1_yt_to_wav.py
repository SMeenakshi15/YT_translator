# # Import necessary libraries
# from pytube import YouTube  # For downloading YouTube videos
# import io
# import tempfile
# from moviepy.editor import VideoFileClip  # For working with video files

# # Define the URL of the YouTube video you want to download
# video_url = 'https://youtu.be/5b5EhSSEvx0'

# # Create a YouTube object for the given video URL
# yt = YouTube(video_url)

# # Create byte stream objects to store video and audio data
# yt_video = io.BytesIO()
# yt_audio = io.BytesIO()

# # Get the highest resolution video stream available
# videoStream = yt.streams.get_highest_resolution()

# # Download the video stream and store it in yt_video byte stream
# videoStream.stream_to_buffer(yt_video)

# # Create a temporary video file with a .mp4 extension
# with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
#     temp_file.write(yt_video.getvalue())
#     video_file_path = temp_file.name

# # Create a VideoFileClip object from the downloaded video file
# my_clip = VideoFileClip(video_file_path)

# # Extract the audio from the video clip
# audio = my_clip.audio

# # Create a temporary audio file with a .wav extension
# with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_temp_file:
#     audio.write_audiofile(audio_temp_file.name)
#     audio_temp_file.seek(0)
#     yt_audio = io.BytesIO(audio_temp_file.read())

# # Save the extracted audio to a file named 'extracted_audio(2).wav'
# with open('extracted_audio(2).wav', 'wb') as audio_file:
#     audio_file.write(yt_audio.read())


# 1_yt_to_wav.py
# Import necessary libraries

import sys
from pytube import YouTube  # For downloading YouTube videos
import io
import tempfile
from moviepy.editor import VideoFileClip  # For working with video files

# Get the YouTube video URL from the command-line argument
video_url = sys.argv[1]

# Create a function to download audio from a YouTube video
def download_audio_from_youtube(video_url):
    # Create a YouTube object for the given video URL
    yt = YouTube(video_url)
    # Create byte stream objects to store video and audio data
    yt_video = io.BytesIO()
    yt_audio = io.BytesIO()

    # Get the highest resolution video stream available
    videoStream = yt.streams.get_highest_resolution()

    # Download the video stream and store it in yt_video byte stream
    videoStream.stream_to_buffer(yt_video)

    # Create a temporary video file with a .mp4 extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(yt_video.getvalue())
        video_file_path = temp_file.name

    # Create a VideoFileClip object from the downloaded video file
    my_clip = VideoFileClip(video_file_path)

    # Extract the audio from the video clip
    audio = my_clip.audio

    # Create a temporary audio file with a .wav extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_temp_file:
        audio.write_audiofile(audio_temp_file.name)
        audio_temp_file.seek(0)
        yt_audio = io.BytesIO(audio_temp_file.read())

    # Save the extracted audio to a file named 'extracted_audio(2).wav'
    with open('extracted_audio(2).wav', 'wb') as audio_file:
        audio_file.write(yt_audio.read())

if __name__ == "__main__":
    download_audio_from_youtube(video_url)