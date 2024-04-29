from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_drag_and_drop(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testautomationpractice.blogspot.com/')
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        scroll = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID, 'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(2)
        self.driver.close()