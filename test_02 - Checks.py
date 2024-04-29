from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Checks(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID,"cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.ID,"male").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"female").click()
        check=self.driver.find_elements(By.CLASS_NAME,"form-check-input")
        print("número de elementos: " + str(check))
        check[2].click()
        time.sleep(0.5)
        check[3].click()
        time.sleep(0.5)
        check[4].click()
        time.sleep(0.5)
        check[5].click()
        time.sleep(0.5)
        check[6].click()
        time.sleep(0.5)
        check[7].click()
        time.sleep(0.5)
        check[8].click()
        time.sleep(1)
        self.driver.close()
