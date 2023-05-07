import speech_recognition as sr
from .speaker import Speaker
from .functions import Functions
from . import lines
from .paths import paths

import subprocess
import sys
import os
import random

from decouple import config


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = Speaker()
        self.fn = Functions()
        self.name = config("BOTNAME")

    def passive_listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.pause_threshold = 0.5

            while True:
                audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio, language='pt-BR')
                    print("Transcrição: " + text)
                    if self.name.lower() in text.lower():
                        print("aq")
                        return self.listen()
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print("Erro: {0}".format(e))

    def listen(self):
        with sr.Microphone() as source:
            self.speaker.speak(random.choice(lines.listening))
            
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)
            
            self.speaker.speak(random.choice(lines.handling))
        
        data = ""

        try:
            data = self.recognizer.recognize_google(audio, language='pt-BR')
            self.handler(data.lower())
        except sr.UnknownValueError:
            self.speaker.speak("Desculpe, não consegui entender o que foi dito. Pode repetir?")
            self.listen()
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))

        return data

    def handler(self, data):
        print(data)
    
        if "hora" in data:
            self.fn.getTime()

        if "editor de texto" in data:
            editor = "open" if sys.platform == "darwin" else "xed"
            subprocess.run([paths.get('editor de texto')])
        
        self.passive_listen()
