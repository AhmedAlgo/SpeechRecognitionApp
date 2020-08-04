import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random
from time import ctime
import time
import webbrowser


reco = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Areny_speaks(ask)
        audio = reco.listen(source)
        voice_data=''
        try:
            voice_data= reco.recognize_google(audio)
            #Areny_speaks(voice_data)
        except sr.UnknownValueError:
            Areny_speaks('Sorry, I did not understand that')
        except sr.RequestError:
            Areny_speaks('Sorry, the server is not working') 
        
        return voice_data

def responed(voice_data):
    if 'hello' in voice_data:
        Areny_speaks('hello') 
    if 'what is your name' in voice_data:
        Areny_speaks('my name is Areny')    
    if 'what is the time' in voice_data:
        Areny_speaks(ctime())
    if 'how are you' in voice_data:
        Areny_speaks('I am good, thank you')
    if 'exit' in voice_data:
        Areny_speaks('exiting now have a nice day')
        exit()
    if 'find information' in voice_data:
        information = record_audio('what do you want to know about')
        url = 'https://google.com/search?q=' + information
        webbrowser.get().open(url)
        Areny_speaks('Here is the information you requested about' + information)
    if 'find location' in voice_data:
        location = record_audio('where do want to go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Areny_speaks('Here is the location of' + location)

    


def Areny_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r= random.randint(1, 1000)
    audio_file= 'audio-' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
Areny_speaks('How May I help?')
while 1:
    voice_data = record_audio()
    responed(voice_data)

