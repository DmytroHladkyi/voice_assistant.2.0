import os
import random
import speech_recognition 
import time
import pyttsx3
import fnmatch

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
            print("Nie rozpoznałem")
            speak("Nie rozpoznałem")
            continue
        
def open_todo_list():
    with open ('todo-list.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        time.sleep(0.5)
        if os.path.getsize(r'C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\todo-list.txt') == 0:
            speak('Nie masz tam nic')
            return "Notatka jest pusta"
        else:    
            speak('Oto lista zadań:')
            # print(content)
            speak(content)
            return content