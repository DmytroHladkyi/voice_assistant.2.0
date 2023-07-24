import speech_recognition 
import pyttsx3
import pygame
from play_music import play_music
from create_task import create_task
from remove_task import remove_task
from open_todo_list import open_todo_list
from searching_file import searching_file
from weather import main1
from sending_email import main2
from searching_info import main3
from chat_gpt import main6
# from test import main10




sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7

commands_dict = {
    'commands': {
        'greeting': ['witaj', 'cześć'],
        'create_task': ['dodać notatkę', 'notatka'],
        'play_music': ['muzyka', 'włącz muzykę'],
        'open_todo_list': ['otwórz notatkę', 'pokaż notatkę'],
        'remove_task': ['usuń notatkę'],
        'searching_file': ['chcę znaleźć folder', 'folder', 'plik'],
        'main2': ['poczta'],
        'main1': ['pogoda'],  
        'main3': ['wyszukiwanie'],
        'main6': ['gpt'],
        # 'main10': ['test'],
    }  
}

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
            continue
         
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

def greeting():
    speak('Witam Ciebie!')
    return 'Witam Ciebie!'

def main():
    stop_words = ['stop','kończymy na dzisiaj','kończymy', 'nara']
    speak('Witam Ciebie')
    print("To jest Twój asystent głosowy. Aby zacząć ze mną rozmiawiać powiedz 'okej'")
    sound_played = False
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                if not sound_played:
                    play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                    sound_played = True
                audio = sr.listen(source=mic, timeout=10)
                queryword = sr.recognize_google(audio_data=audio, language='pl').lower()
                if queryword.lower() == "okej":
                    sound_played = False
                    print("W czym moge pomóc.\nJa mogę przywitać Ciebie.\nJa mogę dodawać notatki.\nMogę je usuwać lub wyświetlać je.\nMogę odtważać muzykę.\nMogę wyszukiwać plik na komputerze.\nMogę sprawdzać jaka jest pogoda w mieście, który chcesz spawdzić.\nMogę pomoć Ci wysłać pocztę mailową.\nMogę również znaleźć dla Ciebie co będziesz chciał na youtube czy w google.\nMogę podłaczyć Ciebie do Chatu GPT.")
                    speak("W czym moge pomóc")
                    if not sound_played:
                        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
                        sound_played = True
                    query = listen_command()
                    sound_played = False
                    
                    if any(word in query for word in stop_words):
                        print('Do zobaczenia!')
                        speak('Do zobaczenia!')
                        break
                    
                    command_found = False
                    for k, v in commands_dict['commands'].items():
                        if query in v:
                            print(globals()[k]())
                            command_found = True
                            speak("Co chcesz jeszcze?")
                            print("Aby kontynuować powiedz 'okej'")
                            sound_played = False
                            break
                elif any(word in queryword for word in stop_words):
                    print('Do zobaczenia!')
                    speak('Do zobaczenia!')
                    break
        
            if not command_found:
                print(f"Nie znaleziono komendy '{query}'")
                speak(f"Nie znaleziono komendy '{query}'")
                print("Aby kontynuować powiedz 'okej'")
                
        except Exception as e: 
            # print("Ошибка сервиса распознавания речи: {0}".format(e))
            continue

if __name__ == '__main__':
    main()