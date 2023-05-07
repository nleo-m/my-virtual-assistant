from .speaker import Speaker
from datetime import datetime
from decouple import config

class Functions:
    def __init__(self):
        self.speaker = Speaker()
        self.name = config("BOTNAME")
        self.user = config("USERNAME")

    def getTime(self):
        now = datetime.now()
        hour = now.hour
        minutes = now.minute
        seconds = now.second

        self.speaker.speak(f"Agora são {hour} horas, {minutes} minutos e {seconds} segundos.")

    def greet(self):
        hour = datetime.now().hour
        if hour >=6 and hour <= 11:
            self.speaker.speak(f"Bom dia {self.user}!")
        elif hour >=12 and hour <=17:
            self.speaker.speak(f"Boa tarde {self.user}!")
        else:
            self.speaker.speak(f"Boa noite {self.user}!")