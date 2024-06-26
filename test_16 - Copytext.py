# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_Automation_Test_Practice():

    def test_Copytext(self):
      self.driver = webdriver.Chrome()
      self.driver.get("https://testautomationpractice.blogspot.com/")
      self.driver.maximize_window()
      try:
        self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
      except:
        pass
      self.driver.set_window_size(1936, 1056)
      self.driver.find_element(By.ID, "field1").click()
      self.driver.find_element(By.CSS_SELECTOR, ".column-right-inner > aside").click()
      self.driver.find_element(By.ID, "field1").send_keys("Copiando Texto")
      time.sleep(2)

      self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click()
      self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)")
      actions = ActionChains(self.driver)
      actions.double_click(element).perform()
      time.sleep(2)
      value1 = self.driver.find_element(By.ID, "field1").get_attribute("value")

      value2 = self.driver.find_element(By.ID, "field2").get_attribute("value")
      assert value1 == value2
      time.sleep(2)
      self.driver.close()
  
