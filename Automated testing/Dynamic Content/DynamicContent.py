import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import unittest

class MainDynamicTest (unittest.TestCase):
    def test_dynamic(self):
        S = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=S)
        #Cargar la página por primera vez
        LoadPage(driver)
        #Validar si la página tiene imágenes y textos iguales - Iguales = True , Diferentes = False
        HayRepetidos = CheckContent(driver)

        ButtonRefresh = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/p[2]/a')
        RefreshTimes = 0
        while HayRepetidos:
            RefreshTimes= RefreshTimes + 1
            ButtonRefresh.click()
            HayRepetidos = CheckContent(driver)
        if RefreshTimes == 0:
            print("No hay datos repetidos")
        else:
            print("Refresh Number " + str(RefreshTimes))

        print("End")
        time.sleep(3) # espera 3 segundos para validar resultado
        driver.stop_client()
        driver.quit()


def CheckContent (driver):
    #Obtener Una lista de los rows de la página

    Container  = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div')
    Filas = Container.find_elements(by=By.CLASS_NAME, value='row')

    Imagenes = []
    Textos = []
    for x in Filas:
        Imagen = ''
        Texto = ''
        Imagen = x.find_element(by=By.CLASS_NAME, value='large-2').find_element(by=By.TAG_NAME, value='img').get_attribute('src')
        Texto = x.find_element(by=By.CLASS_NAME, value='large-10').text
        Imagenes.append(Imagen)
        Textos.append(Texto)

    ImagenesRepetidas = False
    TextosRepetidos = False
    if len(Imagenes) == len(set(Imagenes)):
        ImagenesRepetidas = False
    else:
        ImagenesRepetidas = True

    if len(Textos) == len(set(Textos)):
        TextosRepetidos = False
    else:
        TextosRepetidos = True

    if ImagenesRepetidas == True:
        return True
    elif TextosRepetidos == True:
        return True
    else:
        return False


def LoadPage(driver):
    driver.get('https://ss-testing-automated-exercise.herokuapp.com/dynamic_content')


if __name__ == '__main__':
    unittest.main()