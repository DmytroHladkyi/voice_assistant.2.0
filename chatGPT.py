import openai
import speech_recognition as sr
import pyttsx3
from api_key import apikey
import pygame
import datetime
import re

openai.api_key = apikey
# # инициализировать библиотеку для генерации речи
engine = pyttsx3.init()


def listen_command(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="pl")
        # return recognizer.recognize_google(audio) /////ENG
    except:
        print("Nie rozpoznałem")
        speak("Nie rozpoznałem")
        
                           
        

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.5,
        n=1,
        stop=None,
)
    return response["choices"][0]["text"]

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

def get_local_time():
    local_time = datetime.datetime.now().time()
    return str(local_time)


def main4():
    sound_played = False
    filename = "input.wav"
    print("Zadaj pytanie.")
    speak("Zadaj pytanie.")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                if not sound_played:
                    play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                    sound_played = True
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                answer = recognizer.recognize_google(audio, language="pl")
                if answer.lower() != "stop":
                    source.pause_threshold = 0.7
                    with open (filename, "wb") as f:
                        f.write(audio.get_wav_data())
                    text = listen_command(filename)
                    if text:
                        if re.search(r'\b(jaka|która).*godzina\b', text.lower()):
                            current_time = datetime.datetime.now().strftime("%H:%M")
                            print(f'Aktualna godzina to: {current_time}')
                            speak(f'Aktualna godzina to: {current_time}')
                            print("Zadaj pytanie lub 'stop' jeżeli chcesz wyjść z rozmowy.")   
                            sound_played = False  
                        else:
                            print(f'You said: {text}?')
                            response = generate_response(text)
                            print(f'GPT says: {response}')
                            speak(response)
                            print("Zadaj pytanie lub 'stop' jeżeli chcesz wyjść z rozmowy.")   
                            sound_played = False  
            
                else:
                    answer.lower() == "stop"
                    sound_played = False
                    break
        except Exception as e:
            continue

if __name__ == '__main__':
    main4()