import openai
import json
from base64 import b64decode
import speech_recognition as sr
import pyttsx3
import os
from api_key import apikey
import pygame


def speak(text):
    """Произносит текст"""
    engine.setProperty('rate', 128, )
    engine.say(text)
    engine.runAndWait()
# инициализировать библиотеку для генерации речи
engine = pyttsx3.init()

def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


def main5():
    print("Powiedz co chcesz:")
    speak("Powiedz co chcesz:")
    sound_played = False
    while True:
        try:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                source.pause_threshold = 1
                if not sound_played:
                    play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                    sound_played = True
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                # prompt = recognizer.recognize_google(audio, language="pl")
                prompt = recognizer.recognize_google(audio, language="en") 
                if prompt != "stop":
                    print(f'Powiedziałeś: {prompt}')
                    speak(f'Powiedziałeś: {prompt}')

                    openai.api_key = apikey

                    response = openai.Image.create(
                        prompt=prompt,
                        n=1,
                        size='512x512',
                        response_format='b64_json'
                    )

                    with open('data.json', 'w') as file:
                        json.dump(response, file, indent=4, ensure_ascii=False)

                    image_data = b64decode(response['data'][0]['b64_json'])
                    file_name = '_'.join(prompt.split(' '))

                    if not os.path.exists('photos'):
                        os.makedirs('photos')

                    # Путь к файлу внутри папки "photos"
                    file_path = os.path.join('photos', f'{file_name}.png')

                    with open(file_path, 'wb') as file:
                        file.write(image_data)
                        print(f"Zdjęcie {file_name} zostało zapisane w folderze {file_path}")
                        speak("Zdjęcie zrobione.")
                        print("Powiedz co chcesz:")
                        speak("Powiedz co chcesz:")
                        sound_played = False
                        
                else:
                    prompt = "stop"
                    sound_played = False
                    break    
        except Exception as e:
                continue 
     
                        
if __name__ == '__main__':
    main5()