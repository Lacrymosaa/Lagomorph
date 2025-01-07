from wikipedia import summary
import webbrowser
from urllib.parse import quote
import os

def searchGoogle(query):
    if "google" in query:
        query = query.replace("pesquisar no google ", "")
        query = query.replace("pesquisa ", "")
        query = query.replace("pesquise ", "")
        query = query.replace("no google ", "")
        query = query.replace("google ", "")
        
    try:
        url = f"https://www.google.com/search?q=" + query
        webbrowser.open(url)
        return "Pesquisa no Google aberta no navegador padrão."
    except Exception as e:
        print("Erro ao pesquisar no Google:", e)
        return "Desculpe, não consegui abrir a pesquisa no Google."

def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("pesquisar no youtube ", "")
        query = query.replace("youtube ", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        return "Pronto, mestre!"
