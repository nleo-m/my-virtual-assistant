import speech_recognition as sr
from .speaker import Speaker

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = Speaker()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        
        data = ""

        try:
            data = self.recognizer.recognize_google(audio, language='pt-BR')
        except sr.UnknownValueError:
            self.speaker.speak("Desculpe, não consegui entender o que foi dito.")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))

        return data