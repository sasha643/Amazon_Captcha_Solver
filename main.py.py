import easyocr
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

driver = webdriver.Edge()


def getdata(url):
    r = requests.get(url)
    return r.text


L = []

driver.get('https://www.amazon.com/errors/validateCaptcha')

while True:
    htmldata = driver.page_source
    time.sleep(3)
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img'):
            L.append(item['src'])
            url = L[0]
            #print(url)
            L = []
            reader = easyocr.Reader(['en'])
            results = reader.readtext(url)

            for (bbox, text, prob) in results:
                ''
    input = driver.find_element(By.XPATH, "//input[@name='field-keywords']")
    input.send_keys(text)
    time.sleep(2)
    signin_field = driver.find_element(By.XPATH, "//button[@type='submit']")
    signin_field.click()
    time.sleep(2)

    current_url = driver.current_url

    if current_url == 'https://www.amazon.com/':
            print('\ncontiuing the web scraping and successfully solved the captcha!')
            break
    
    else:
          continue
        
driver.quit()