from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Menu_Desplegable(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Canada']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'United Kingdom']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Germany']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'France']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Australia']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Japan']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'China']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Brazil']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'India']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'United States']").click()
        self.driver.close()