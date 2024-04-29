from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Pagination_Table(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) input").click()
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.LINK_TEXT, "3").click()
        self.driver.find_element(By.LINK_TEXT, "4").click()
        self.driver.find_element(By.LINK_TEXT, "1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(3)").text == "$10.99"
        assert self.driver.find_element(By.CSS_SELECTOR,"tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)").text == "Product 4"
        self.driver.close()