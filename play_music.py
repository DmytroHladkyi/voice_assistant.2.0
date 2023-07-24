import os
import random
import pyttsx3
import speech_recognition 
import time

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7


# commands_dict = {
#     'commands': {
#         'greeting': ['witaj', 'cześć'],
#         'create_task': ['dodać notatkę', 'notatka'],
#         'play_music': ['muzyka', 'włącz muzykę'],
#         'open_todo_list': ['otwórz notatkę', 'pokaż notatkę'],
#         'remove_task': ['usuń notatkę'],
#         'searching_file': ['chcę znaleźć folder'],
#     }
# }

# инициализировать библиотеку для генерации речи
engine = pyttsx3.init()

def speak(text):
    """Произносит текст"""
    engine.setProperty('rate', 128, )
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Возвращает распознанную команду"""
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic, timeout=10)
                query = sr.recognize_google(audio_data=audio, language='pl').lower()
                return query
        except speech_recognition.UnknownValueError:
            # print("Nie rozpoznałem")
            # speak("Nie rozpoznałem")
            continue


def play_music():
    """Play a random mp3 file"""
    
    music_folder = 'D:\\Music'
    files = os.listdir(music_folder)
    random_file = random.choice(files)
    os.system(f'start wmplayer "{music_folder}\\{random_file}"')
    speak(f'Włączam muzykę.')
    print(f'Gra {random_file.split("/")[-1]} 🔊🔊🔊')
    
    while True:
        query = listen_command()
        
        if 'dalej' in query:
            random_file = random.choice(files)
            os.system(f'start wmplayer "{music_folder}\\{random_file}"')
            speak(f'Zmieniam.')
            print(f'Gra {random_file.split("/")[-1]} 🔊🔊🔊')
            continue 
        
        elif 'stop muzyka' in query:
            break