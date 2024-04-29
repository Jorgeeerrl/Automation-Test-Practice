from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_iframe_formulario(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.switch_to.frame("frame-one796456169")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID, 'RESULT_TextField-0'))).click()
        self.driver.find_element(By.ID, "RESULT_TextField-0").send_keys("Jorge")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) label").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) label").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".icon_calendar").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "9").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "RESULT_RadioButton-3").click()
        menu = self.driver.find_element(By.ID, "RESULT_RadioButton-3")
        menu.find_element(By.XPATH, "//option[. = 'QA Engineer']").click()
        self.driver.find_element(By.ID, "RESULT_RadioButton-3").click()
        menu = self.driver.find_element(By.ID, "RESULT_RadioButton-3")
        menu.find_element(By.XPATH, "//option[. = 'Automation Engineer']").click()
        self.driver.find_element(By.ID, "RESULT_RadioButton-3").click()
        menu = self.driver.find_element(By.ID, "RESULT_RadioButton-3")
        menu.find_element(By.XPATH, "//option[. = 'Developer']").click()
        self.driver.find_element(By.ID, "RESULT_RadioButton-3").click()
        menu = self.driver.find_element(By.ID, "RESULT_RadioButton-3")
        menu.find_element(By.XPATH, "//option[. = 'Manager']").click()
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit_button")))
        submit_button.click()
        submit_text=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div[3]/div")))
        assert submit_text.text == "The result storage capacity has been reached for this form. Your result was not created. Please contact the form owner."
        self.driver.close()