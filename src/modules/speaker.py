from decouple import config
import pyttsx3
from datetime import datetime

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init('espeak')
        self.engine.setProperty('rate', 90)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', 'mb-br4')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def time(self):
        now = datetime.now()
        hour = now.hour
        minutes = now.minute
        seconds = now.second

        self.speak(f"Agora são {hour} horas, {minutes} minutos e {seconds} segundos.")
