import speech_recognition as sr # library for performing speech recognition
from gtts import gTTS # gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate text-to-speech API
import playsound # play audio files (for more info about this module:https://github.com/TaylorSMarks/playsound)  
import os # remove audio files (
import random # to randomly assign names to the audio files
from time import ctime # to give the module the ability to know the time
import time # to add delay in the execution of the code, without it, the code was runing so fast that it could not accept another voice commands
import webbrowser # a module help the code to open and display the browser.


reco = sr.Recognizer() #initialise a recogniser


def record_audio(ask = False): # a function that can take the user's voice inputs and transform them to texts
    with sr.Microphone() as source: # Microphone is our input source
        if ask:
            Areny_speaks(ask)
        audio = reco.listen(source) # listen for the input using the source (Microphone)
        voice_data=''
        try:
            voice_data= reco.recognize_google(audio) #convert audio to texts
            
        except sr.UnknownValueError: #Raises exception if the speech is unintelligible. 
            Areny_speaks('Sorry, I did not understand that')
        except sr.RequestError: #Raises exception if the speech recognition operation failed, if the key isn't valid, or if there is no internet connection.
            Areny_speaks('Sorry, the server is not working') 
        
        return voice_data

def responed(voice_data): # a function with the possible responses, obviously you can add more  
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
    if 'find information' in voice_data: # search Google for information
        information = record_audio('what do you want to know about')
        url = 'https://google.com/search?q=' + information
        webbrowser.get().open(url)
        Areny_speaks('Here is the information you requested about' + information)
    if 'find location' in voice_data: #find location using Google Maps
        location = record_audio('where do want to go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Areny_speaks('Here is the location of' + location)

    


def Areny_speaks(audio_string): # a function that gets a string a make an audio file
    tts = gTTS(text=audio_string, lang='en') # texts to speech
    r= random.randint(1, 1000) # generate a number for the audio file
    audio_file= 'audio-' + str(r) +'.mp3' # make audio file as mp3
    tts.save(audio_file) # save the audio file
    playsound.playsound(audio_file) # play the audio file
    print(audio_string) # print the subtitle/ what is being said
    os.remove(audio_file) # remove the file


time.sleep(1) # delay the execution of the code for 1 second
Areny_speaks('How May I help?')
while 1:
    voice_data = record_audio() # get the voice input
    responed(voice_data) # respond

