# Extract Audio From Video Using Python..

import moviepy.editor
s = input('Enter the video name: ')  # the video can be any format like mp4...

# if your video file is in the same folder then you can give the name directly..
# else you need to give the path of the video file..

video = moviepy.editor.VideoFileClip(s)

audio = video.audio

a = input('Enter the audio file name: ') # Enter the audio file name to be saved with..

# the audio file will be in mp3 format..

audio.write_audiofile(a)

# audio file will be created in the same directory..
