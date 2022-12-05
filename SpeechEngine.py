# digital assistant incorporating machine learning and intent classing - EPQ 2022 Rishi Thiahulan

#area for library imports
import pyttsx3 as pt
from gtts import gTTS
from io import BytesIO


#

""" def speechEngine(string):
        # initialising text-to-speech engine.
        engine = pt.init() # create object engine

        '''RATE'''
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('rate', 155) # set the rate of speech as number between 0-1
        ''''''

        '''VOLUME'''
        volume = engine.getProperty('volume')
        print(volume)
        engine.setProperty('volume', 1.0) # set the volume level as number between 0-1
        ''''''

        '''VOICE'''
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # set the voice library to use [1 for female, 0 for male]
        ''''''

        engine.say(string)
        engine.runAndWait()
        engine.stop() """

def speechEngine(string):
    mp3_fp = BytesIO()
    tts = gTTS(string, lang='en')
    tts.write_to_fp(mp3_fp)