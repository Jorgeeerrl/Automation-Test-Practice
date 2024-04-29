from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():


    def test_Formulario(self):

        self.driver=webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID,"cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.ID,"name").send_keys("Jorge")
        self.driver.find_element(By.ID,"email").send_keys("jorgeeerrl@jorge.com")
        self.driver.find_element(By.ID,"phone").send_keys("555555555")

        self.driver.find_element(By.ID,"textarea").send_keys("Calle Los Limones, 85")
        script = "document.getElementById('textarea').style.height='200px';"
        self.driver.execute_script(script)
        time.sleep(1)
        script = "document.getElementById('textarea').style.height='50px';"
        self.driver.execute_script(script)
        time.sleep(1)
        self.driver.close()