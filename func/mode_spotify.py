import speech_recognition as sr
import pyttsx3
import os
import speech_recognition as sr
import spotipy
import spotipy.util as util

recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        r.energy_threshold = 21000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, 0, 8)

    try:
        query = r.recognize_google(audio, language='pt-BR')
        return query.lower()
    except Exception as e:
        return ""

def spotify_mode():
    print("Entrando no modo Spotify...")
    username = 'Insert username'  
    scope = 'user-read-playback-state,user-modify-playback-state'
    client_id = 'Insert client ID'  
    client_secret = 'Insert client secret'  
    redirect_uri = 'http://localhost:8080'

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    sp = spotipy.Spotify(auth=token)
    
    while True:
        command = listen()
        try:
            if "pausar música" in command:
                sp.pause_playback()
                speak("Música pausada.")
            elif "continuar música" in command:
                sp.start_playback()
                speak("Música despausada.")
            elif "próxima música" in command:
                sp.next_track()
                speak("Próxima música.")
            elif "música anterior" in command:
                sp.previous_track()
                speak("Música anterior.")
            elif "modo aleatório" in command:
                sp.shuffle(True)
                speak("Playlist em modo aleatório.")
            elif "tocar playlist" in command:
                playlist_name = command.split("tocar playlist ")[1]
                playlists = sp.current_user_playlists()['items']
                for playlist in playlists:
                    if playlist['name'].lower() == playlist_name.lower():
                        playlist_id = playlist['id']
                        sp.start_playback(context_uri=f"spotify:playlist:{playlist_id}")
                        speak(f"Tocando a playlist {playlist_name}.")
                        break
                else:
                    speak("Playlist não encontrada.")
            elif "sair" in command:
                return "Saindo do Modo Spotify"
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            speak("Comando incorreto.")
            
    
