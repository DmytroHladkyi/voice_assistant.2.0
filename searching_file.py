import os
import speech_recognition 
import pyttsx3
import fnmatch
import pygame


sr = speech_recognition.Recognizer()
sr.pause_threshold = 1


def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

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


def searching_file():
    sound_played = False
    print("Powiedz jak ma się nazywać folder.")
    speak("Powiedz jak ma się nazywać folder.")
    if not sound_played:
        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
        sound_played = True
    query = listen_command()

    # распознаем речь с помощью Google Speech Recognition
    try:
        print(f"Powiedziałeś: {query}")
        speak(f"Powiedziałeś: {query}")

        # ищем папки на компьютере
        folder_name = query.lower()
        matches = []
        
        for root, dirnames, filenames in os.walk("D:\\"):
            for dirname in dirnames:
                if fnmatch.fnmatch(dirname.lower(), folder_name):
                    matches.append(os.path.join(root, dirname))
                    print(f"Folder {folder_name} znaleziony w {root}")
                    
                    
        if matches:
            for match in matches:
                if os.path.isdir(match):
                    print(match)
                    return(f"Znalezione następujące pliki o nazwie {folder_name}:")  
        else:
            print(f"Folder {folder_name} nie znaleziony na komputrze")
    except speech_recognition.UnknownValueError:
        return "Nie rozpoznałem"