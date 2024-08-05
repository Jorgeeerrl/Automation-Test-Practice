from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class Test_Automation_Test_Practice:

    def setup_method(self, method):

        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument('--window-size=1920,1080')

        project_root = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(project_root, "chromedriver.exe")
        # os.path.dirname(os.path.abspath(__file__)) obtiene la ruta del directorio donde está el script actual.
        # os.path.join(project_root, "chromedriver.exe") construye la ruta completa al chromedriver.exe basado en ello.

        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        self.driver.get("https://testautomationpractice.blogspot.com/")

    def teardown_method(self, method):
        self.driver.quit()


