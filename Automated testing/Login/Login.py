import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import unittest

class MainLoginTest (unittest.TestCase):
    def test_ValidCredentials(self):
        S = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=S)
        LoadPage(driver)
        PUsername = 'tomsmith'
        PPassword = 'SuperSecretPassword!'
        FillForm(driver, PUsername, PPassword)
        Submit = driver.find_element(by=By.XPATH, value='//*[@id="login"]/button')
        Submit.click()
        time.sleep(2)
        LogoutButton = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/a')
        if len(LogoutButton.get_attribute('href')):
            print("Prueba con Datos válidos")
            print("Login exitoso")
            time.sleep(2)
            print("Realizar el deslogueo")
            driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/a').click()
            time.sleep(2)
            driver.refresh()
        else:
            print("Logueo no exitoso")
        time.sleep(3)  # espera 5 segundos para validar resultado
        driver.stop_client()
        driver.quit()


    def test_NotValidCredentials(self):
        S = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=S)
        LoadPage(driver)
        Submit = driver.find_element(by=By.CLASS_NAME, value='radius')
        RefreshLogginButton(driver)
        print("Prueba con Datos No válidos")
        #Validar campos vacíos.
        PUsername = ''
        PPassword = ''
        FillForm(driver, PUsername, PPassword)
        time.sleep(1)
        Submit.click()
        print("Datos no válidos, campos vacíos")
        time.sleep(2)
        driver.refresh()
        #Validar usuarios inválidos
        RefreshLogginButton(driver)
        PUsername = 'username'
        PPassword = 'passworasdasdd'
        FillForm(driver, PUsername, PPassword)
        time.sleep(1)
        Submit = driver.find_element(by=By.CLASS_NAME, value='radius')
        Submit.click()
        print("Usuario inválido")
        time.sleep(2)
        driver.refresh()
        #Validar usuario con contraseña errónea
        RefreshLogginButton(driver)
        PUsername = 'tomsmith'
        PPassword = 'password'

        FillForm(driver, PUsername, PPassword)
        time.sleep(1)
        Submit = driver.find_element(by=By.CLASS_NAME, value='radius')
        Submit.click()
        print("Usuario existe, pero contraseña errónea")
        time.sleep(2)
        driver.refresh()
        time.sleep(2)  # espera 5 segundos para validar resultado
        driver.stop_client()
        driver.quit()

def RefreshLogginButton(driver):
    Submit = driver.find_element(by=By.XPATH, value='//*[@id="login"]/button')

def FillForm(driver, username, password):
    Username = driver.find_element(by=By.ID, value='username')
    Password = driver.find_element(by=By.ID, value='password')
    Username.send_keys(username)
    Password.send_keys(password)

def LoadPage(driver):
    driver.get('https://ss-testing-automated-exercise.herokuapp.com/login')


if __name__ == '__main__':
    unittest.main()