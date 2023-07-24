import speech_recognition as sr
import pyttsx3
from api_key import apikey
from base64 import b64decode
from chatGPT import main4
from chatGPT_image import main5
import pygame


# # инициализировать библиотеку для генерации речи
engine = pyttsx3.init()


def speak(text):
    """Произносит текст"""
    engine.say(text)
    engine.runAndWait()

def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def main6():
    sound_played = False
    while True:
        print("Powiedz 'czat' aby zacząć rozmowę lub 'zdjęcie', aby zakończyć rozmowę powiedz 'stop'.")
        speak("Powiedz czat lub zdjęcie.")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            if not sound_played:
                    play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                    sound_played = True
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language="pl")
                if transcription.lower() == "czat":
                    main4()
                    sound_played = False
                elif transcription.lower() == "zdjęcie":  
                    main5()
                    sound_played = False
                elif transcription.lower() == "stop": 
                    sound_played = False
                    break
            except Exception as e:
                print("")

if __name__ == '__main__':
    main6()
