from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Calendario(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "datepicker")))
        self.driver.find_element(By.ID,"datepicker").click()
        self.driver.find_element(By.CLASS_NAME,"ui-datepicker-prev").click()
        self.driver.find_element(By.CLASS_NAME,"ui-datepicker-next").click()
        self.driver.find_element(By.XPATH,"//a[contains(.,'12')]").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"datepicker").click()
        self.driver.find_element(By.XPATH,"//a[contains(.,'24')]").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"datepicker").click()
        self.driver.find_element(By.ID,"datepicker").clear()
        self.driver.find_element(By.ID,"datepicker").send_keys("23/04/2025")
        self.driver.close()