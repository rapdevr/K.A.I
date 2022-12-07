from gtts import gTTS
import os
 
tts = gTTS(text="Hello", lang="en")
filename = "hello2.mp3"
tts.save(filename)
os.system(f"start {filename}")