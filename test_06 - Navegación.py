
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():

    def test_Navegacion(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        link=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='post-body-1307673142697428135']/a[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        link.click()
        time.sleep(1)
        url_now=self.driver.current_url
        assert url_now=="https://demo.opencart.com/"
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH,"//*[@id='post-body-1307673142697428135']/a[2]").click()
        time.sleep(1)
        url_now=self.driver.current_url
        assert url_now=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver.back()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"home-link").click()
        url_now=self.driver.current_url
        assert url_now=="https://testautomationpractice.blogspot.com/"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "feed-link"))).click()
        time.sleep(1)
        self.driver._switch_to.window(self.driver.window_handles[1])
        url_now = self.driver.current_url
        assert url_now == "https://testautomationpractice.blogspot.com/feeds/posts/default"
        self.driver.close()
        self.driver._switch_to.window(self.driver.window_handles[0])
        self.driver.close()