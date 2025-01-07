from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless") 

s = Service('func/geckodriver.exe')  
driver = webdriver.Firefox(service=s, options=options)

url = 'https://www.google.com/search?q=temperatura+em+%C3%A1lvares+machado'

driver.get(url)

temperatura_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="wob_tm"]'))
)
descricao_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="wob_dc"]'))
)

temperatura_texto = temperatura_element.text
descricao_texto = descricao_element.text
driver.quit()


