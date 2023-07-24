import speech_recognition 
import pyttsx3
import pywhatkit
import pygame
from gtts import gTTS





sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7

def speakpl(text):
    engine.setProperty('rate', 128)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


def speak_ru(text):
    # Создаем объект движка
    engine = pyttsx3.init()

    # Получаем список доступных голосов
    voices = engine.getProperty('voices')

    # Ищем русский голос
    russian_voice = None
    for voice in voices:
        if "Russian" in voice.name:
            russian_voice = voice
            break

    # Если найден русский голос, устанавливаем его
    if russian_voice:
        engine.setProperty('voice', russian_voice.id)
    else:
        print("Русский голос не найден")

    # Воспроизводим речь
    engine.say(text)
    engine.runAndWait()

def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Инициализация библиотеки для генерации речи
engine = pyttsx3.init()

def main3():
    sound_played = False
    ask_language = True  # Флаг для повторного вопроса о выборе языка
    print("W jakim języku chcesz wyszukiwać? polski lub rosyjski")
    speakpl("W jakim języku chcesz wyszukiwać? polski lub rosyjski")
    while True:
        if ask_language:  
            try:
                with speech_recognition.Microphone() as mic:
                    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                    if not sound_played:
                        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                        sound_played = True
                    audio = sr.listen(source=mic, timeout=10)
                    transcription = sr.recognize_google(audio_data=audio, language='pl').lower()
                    if transcription.lower() == "polski":
                        sound_played = False
                        ask_language = False  # Устанавливаем флаг в False, чтобы не задавать вопрос о выборе языка
                        print("Powiedziałeś polski")
                        print("Co chcesz znaleźć?")
                        speakpl("Co chcesz znaleźć?")
                        while True:
                            try:
                                with speech_recognition.Microphone() as mic:
                                    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                                    if not sound_played:
                                        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                                        sound_played = True
                                    audio = sr.listen(source=mic, timeout=10)
                                    query_pl = sr.recognize_google(audio_data=audio, language='pl').lower()
                                    if "youtube" in query_pl:
                                        print(f'Powiedziałeś {query_pl}.')
                                        speakpl(f'Powiedziałeś {query_pl}.')
                                        pywhatkit.playonyt(query_pl)
                                        print("Jeżeli chcesz wrócić do wyboru języków powiedz 'stop'.")
                                        print("Co chcesz znaleźć?")
                                        speakpl("Co chcesz znaleźć?")
                                        sound_played = False
                                        
                                    elif "stop" in query_pl:
                                        sound_played = False
                                        ask_language = True
                                        print("W jakim języku chcesz wyszukiwać lub powiedz 'stop' aby wyjść do głównego menu?")
                                        speakpl("W jakim języku chcesz wyszukiwać?")
                                        break
                                    else:
                                        print(f'Powiedziałeś {query_pl}.')
                                        speakpl(f'Powiedziałeś {query_pl}.')
                                        pywhatkit.search(query_pl)
                                        print("Jeżeli chcesz wrócić do wyboru języków powiedz 'stop'.")
                                        print("Co chcesz znaleźć?")
                                        speakpl("Co chcesz znaleźć?")
                                        sound_played = False
                                        
                            except speech_recognition.UnknownValueError:
                                continue
                    elif transcription.lower() == "rosyjski":
                        sound_played = False
                        ask_language = False  # Устанавливаем флаг в False, чтобы не задавать вопрос о выборе языка
                        print("Powiedziałeś rosyjski")
                        print("Что ищешь?")
                        speak_ru("Что ищешь?")
                        while True:
                            try:
                                with speech_recognition.Microphone() as mic:
                                    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                                    if not sound_played:
                                        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                                        sound_played = True
                                    audio = sr.listen(source=mic, timeout=10)
                                    query_ru = sr.recognize_google(audio_data=audio, language='ru').lower()
                                    if "youtube" in query_ru:
                                        print(f'Вы сказали: {query_ru}.')
                                        speak_ru(f'Вы сказали: {query_ru}.')
                                        sound_played = False
                                        pywhatkit.playonyt(query_ru)
                                        print("Если вы хотите вернуться к выбору языка, скажите 'стоп'")
                                        print("Что ищешь?")
                                        speak_ru("Что ищешь?")
                                        
                                    elif "стоп" in query_ru:
                                        sound_played = False
                                        print("W jakim języku chcesz wyszukiwać lub powiedz 'stop' aby wyjść do głównego menu?")
                                        speakpl("W jakim języku chcesz wyszukiwać?")
                                        ask_language = True
                                        break
                                    else:
                                        print(f'Вы сказали: {query_ru}.')
                                        speak_ru(f'Вы сказали: {query_ru}.')
                                        sound_played = False
                                        pywhatkit.search(query_ru)
                                        print("Если вы хотите вернуться к выбору языка, скажите 'стоп'")
                                        print("Что ищешь?")
                                        speak_ru("Что ищешь?")
                                        
                            except speech_recognition.UnknownValueError:
                                continue
                    elif transcription.lower() == "stop":
                        return
            except Exception as e:
                continue


if __name__ == '__main__':
    main3()