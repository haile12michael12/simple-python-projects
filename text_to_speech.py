from gtts import gTTS  # We have imported this to convert the text to mp3 audio

s = input("Enter the File name: ") # enter the txt file name

f = open(s)
text = f.read()

obj = gTTS(text= text, lang= 'en' ,slow= False) # en -- english || You can change slow value into True..

f1 = input("Enter the Audio name to be saved : ")  # enter the audio file name that will be auto generated.

obj.save(f1)  # audio file will auto saved in the same directory
