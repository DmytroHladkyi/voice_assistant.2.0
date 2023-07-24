import speech_recognition 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pyttsx3
from gmail_password import gmail_password
import pygame

def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue



sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.7

def listen_command1():
    """Возвращает распознанную команду"""
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query1 = sr.recognize_google(audio_data=audio, language='pl').capitalize()
                return query1
        except speech_recognition.UnknownValueError:
            print("Nie rozpoznałem. Powtórz.")
            continue 

def listen_command2():
    """Возвращает распознанную команду"""
    
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query2 = sr.recognize_google(audio_data=audio, language='pl').capitalize()
                return query2
        except speech_recognition.UnknownValueError:
            print("Nie rozpoznałem. Powtórz.")
            continue 
def listen_command3():
    """Возвращает распознанную команду"""
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query3 = sr.recognize_google(audio_data=audio, language='pl').lower()
                return query3
        except speech_recognition.UnknownValueError:
            print("Nie rozpoznałem. Powtórz.")
            continue 

def speak(text):
    """Произносит текст"""
    engine.setProperty('rate', 128, )
    engine.say(text)
    engine.runAndWait()
# инициализировать библиотеку для генерации речи
engine = pyttsx3.init()
    
# Создайте функцию для распознавания речи с помощью SpeechRecognition
def get_audio():
    sound_played = False
    print("Jaki będzie temat wiadomości:")
    speak("Jaki będzie temat wiadomości:")
    if not sound_played:
        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
        sound_played = True
    query1 = listen_command1()
    # Преобразование речи в текст для темы письма
    try:
        print(f"Temat wiadomości: {query1}")
        speak(f"Temat wiadomości: {query1}")
        
    except speech_recognition.UnknownValueError:
        print("Nie rozpoznałem. Powtórz.")
    
    sound_played = False
    print("Jaka będzie treść wiadomości: ")
    speak("Jaka będzie treść wiadomości: ")
    if not sound_played:
        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
        sound_played = True
    query2 = listen_command2()
    # Преобразование речи в текст для текста сообщения
    try:
        print(f"Treść wiadomości: {query2}")
        
    except speech_recognition.UnknownValueError:
        print("Не удалось распознать речь для текста сообщения.")
    # except sr.RequestError as e:
    #     print(f"Не удалось получить результат от службы распознавания речи: {e}")
    #     return ""


    # Введите учетные данные для отправки электронной почты
    gmail_user = "dmytrogladkyi8@gmail.com"
    

    # Запросите у пользователя текст сообщения
    subject = query1
    body = f"""{query2}.


Best regards,
Me
"""

    receivers = {
    "sobie": "dmytrogladkyi8@gmail.com",
    "ja": "dmytrogladkyi8@gmail.com",
    "mamie": "iryna.gladka70@gmail.com",
    "znajoma": "utochka2312@gmail.com",
    }
    sound_played = False
    print("Komu chcesz wysłać:")
    speak("Komu chcesz wysłać:")
    if not sound_played:
        play_sound(r"C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\zvuk-siri-pered-otvetom.mp3")
        sound_played = True
    query3 = listen_command3()
    while True:
        try:
            # if email:
                # Email найден, продолжайте выполнение кода
            print("Znaleziono adres e-mail.")
            print(f'Odbiorca: "{query3}".')
            speak(f'Odbiorca: "{query3}".')
            email = receivers.get(query3)
            # Ваш код для отправки письма
            
            # else:
            #     # Email не найден
            #     raise KeyError
        except KeyError:
            print(f'Nie znaleziono adresu e-mail dla "{query3}".')
            speak(f'Nie znaleziono adresu e-mail dla "{query3}".')
            

        # Запросите у пользователя адрес электронной почты получателя
        to = email
        
        if to:
            print(f"Odbiorca: {to}")
            break
        else:
            print(f'Nie znaleziono adresu e-mail dla "{query3}".')
            speak(f'Nie znaleziono adresu e-mail dla "{query3}".')
            print("Komu chcesz wysłać:")
            speak("Komu chcesz wysłać:")
            query3 = listen_command3()
            continue
        

    # Отправить сообщение с помощью SMTP-сервера Gmail
    try:
        message = MIMEMultipart()
        message['From'] = gmail_user
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))
        text = message.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, text)
        server.quit()
        speak("Wiedomość została wysłana!")
        print("Wiedomość została wysłana!")
    except Exception as e:
        print("Ошибка отправки сообщения:", e)
        server.quit()

def main2():
    get_audio()

if __name__ == '__main__':
    main2()