from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Colors(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.XPATH,"//*[@id='colors']/option[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='colors']/option[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='colors']/option[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='colors']/option[4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='colors']/option[5]").click()
        time.sleep(1)
        select_elem = Select(self.driver.find_element(By.ID, "colors"))
        select_elem.deselect_all()
        num_options = len(select_elem.options)
        for indice in range(num_options):
            select_elem.deselect_all()
            select_elem.select_by_index(indice)
            time.sleep(1)
        self.driver.close()