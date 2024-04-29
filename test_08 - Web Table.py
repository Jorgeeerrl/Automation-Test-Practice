from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Web_Table(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='HTML1']/div[1]/table")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        tabla = self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
        for fila in tabla:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            datos_fila = [celda.text for celda in celdas if celda.text]
            if datos_fila:
                print("")
                print(datos_fila)

        print("")
        print("")

        tabla = self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
        for fila in tabla:
            celdas_encabezado = fila.find_elements(By.TAG_NAME, "th")
            if celdas_encabezado:
                datos_fila = [celda.text for celda in celdas_encabezado if celda.text.strip()]
                print("")
                print("Encabezado:", datos_fila)
            else:
                celdas_datos = fila.find_elements(By.TAG_NAME, "td")
                datos_fila = [celda.text for celda in celdas_datos if celda.text.strip()]
                print("")
                print("Datos de fila:", datos_fila)

        datos_esperados = ["Learn Selenium", "Learn Java", "Master In Selenium"]
        datos_tabla = [celda.text for fila in tabla for celda in fila.find_elements(By.TAG_NAME, "td")]
        for dato in datos_esperados:
            assert dato in datos_tabla, f"{dato} no encontrado en la tabla"
        print("")
        print("Todos los datos esperados están presentes.")
        self.driver.quit()