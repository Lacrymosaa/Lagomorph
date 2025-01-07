from func.greetings import greetings
from func.search import searchGoogle, searchYoutube
from func.wheater import  getWeather
from func.mode_spotify import spotify_mode
from func.whatsapp import  sendWhatsAppMessage
import speech_recognition as sr
import pyttsx3
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 210)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.pause_threshold = 0.6
        r.energy_threshold = 26000
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source, 0, 8)

    try:
        query = r.recognize_google(audio, language='pt-BR')
        return query.lower()
    except Exception as e:
        return ""

def Lagomorfo():
    name = "lagomorfo"
    while True:
        command = listen()
        if name in command:
            speak("Sim?")
            command = listen()
            while True:
                if "obrigado" in command:
                    speak("Por nada")
                    break
                if "abrir spotify" in command:
                    os.system("start spotify")
                    print("Abrindo Spotify...")
                if "abrir firefox" in command:
                    os.system("start firefox")
                    print("Abrindo Firefox")
                if "google" in command:
                    text = searchGoogle(command)
                    speak(text)
                if "youtube" in command:
                    text = searchYoutube(command)
                    speak(text)
                if "clima" in command:                  
                    speak("Pesquisando...")
                    text = getWeather()
                    speak(text)
                if "modo spotify" in command:
                    text = spotify_mode()
                    speak(text)
                if "mensagem" in command:
                    speak("Mandar mensagem para qual contato?")
                    contato = listen()
                    speak("Conteúdo da mensagem?")
                    content = listen()
                    speak("Esse é o conteúdo da mensagem, deseja enviar?")
                    print("Você disse: " + content)
                    while True:
                        resposta = listen()
                        if "sim" in resposta:
                            result = sendWhatsAppMessage(contato, content)
                            break
                        if "não" in resposta:
                            break
                    speak(result)
                command = listen()
            print("...")


if __name__ == "__main__":
    #start = greetings()
    #speak(start)
    print("!")
    Lagomorfo()
