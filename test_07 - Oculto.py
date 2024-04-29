from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Oculto(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        post_footer_first_div = self.driver.find_element(By.XPATH,"//*[@id='Blog1']/div[1]/div/div/div/div/div[3]/div[1]")
        spans = post_footer_first_div.find_elements(By.TAG_NAME, 'span')
        for span in spans:
            print(span.text)
        self.driver.close()