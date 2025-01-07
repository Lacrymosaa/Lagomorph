from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getWeather():
    try:
        options = Options()
        options.add_argument("--headless") 

        s = Service('func/geckodriver.exe')  
        driver = webdriver.Firefox(service=s, options=options)
        print("Pesquisando.. Aguarde..")

        url = 'https://www.google.com/search?q=temperatura+em+%C3%Cidade'

        driver.get(url)

        temperatura_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wob_tm"]'))
        )
        descricao_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wob_dc"]'))
        )

        temperature = temperatura_element.text
        weather = descricao_element.text
        driver.quit()

        saida = f"A temperatura em Cidade é {temperature}°C e o clima está {weather}."
        return saida
    except Exception as e:
        return f"Ocorreu um erro: {e}"
