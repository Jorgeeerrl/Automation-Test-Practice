from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_Automation_Test_Practice():

    def test_Alerta(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.set_window_size(1936, 1056)
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.ID, "field1").click()
        self.driver.find_element(By.CSS_SELECTOR, "#HTML9 button:nth-child(1)").click()
        alert = self.driver.switch_to.alert
        assert alert.text == "I am an alert box!"
        alert.accept()
        self.driver.find_element(By.CSS_SELECTOR, "#HTML9 button:nth-child(2)").click()
        alert = self.driver.switch_to.alert
        assert alert.text == "Press a button!"
        alert.dismiss()
        self.driver.find_element(By.CSS_SELECTOR, "#HTML9 button:nth-child(2)").click()
        alert = self.driver.switch_to.alert
        assert alert.text == "Press a button!"
        alert.accept()
        self.driver.find_element(By.CSS_SELECTOR, "#HTML9 button:nth-child(3)").click()
        alert = self.driver.switch_to.alert
        assert alert.text == "Please enter your name:"
        alert.send_keys("Jorgeeerrl")
        alert.accept()
        assert self.driver.find_element(By.ID, "demo").text == "Hello Jorgeeerrl! How are you today?"
        self.driver.close()