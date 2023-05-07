from decouple import config
import pyttsx3
from datetime import datetime

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init('espeak')
        self.engine.setProperty('rate', 75)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', 'mb-br4')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

