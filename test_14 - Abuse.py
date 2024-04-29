from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Abuse(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(1)
        frame_element = self.driver.find_element(By.ID, "frame-one796456169")
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Report abuse"))).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='RESULT_TextField-5']"))).click()
        self.driver.find_element(By.ID, "RESULT_TextField-5").send_keys("jorge@jorge.com")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) label").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) label").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) label").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) label:nth-child(2)").click()
        self.driver.find_element(By.ID, "RESULT_TextField-6").click()
        self.driver.find_element(By.ID, "RESULT_TextField-6").send_keys("Abuse")
        self.driver.switch_to.frame(0)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "recaptcha-anchor"))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, 'FSsubmit'))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for reporting"
        self.driver.close()