from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Wikipedia(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.CLASS_NAME, "wikipedia-icon").click()
        self.driver._switch_to.window(self.driver.window_handles[1])
        url_now=self.driver.current_url
        assert url_now=="https://en.wikipedia.org/wiki/Main_Page"
        self.driver._switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").click()
        self.driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Valencia CF")
        self.driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "wikipedia-search-result-link")))
        busqueda=self.driver.find_element(By.ID,"wikipedia-search-result-link")
        assert busqueda.text=="Valencia CF"
        self.driver._switch_to.window(self.driver.window_handles[1])
        self.driver.close()