
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Automation_Test_Practice():


    def test_Formulario(self):

        self.driver=webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID,"cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.ID,"name").send_keys("Jorge")
        self.driver.find_element(By.ID,"email").send_keys("jorgeeerrl@jorge.com")
        self.driver.find_element(By.ID,"phone").send_keys("555555555")

        self.driver.find_element(By.ID,"textarea").send_keys("Calle Los Limones, 85")
        script = "document.getElementById('textarea').style.height='200px';"
        self.driver.execute_script(script)
        time.sleep(1)
        script = "document.getElementById('textarea').style.height='50px';"
        self.driver.execute_script(script)
        time.sleep(1)
        self.driver.close()


    def test_Checks(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID,"cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.ID,"male").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"female").click()
        check=self.driver.find_elements(By.CLASS_NAME,"form-check-input")
        print("número de elementos: " + str(check))
        check[2].click()
        time.sleep(0.5)
        check[3].click()
        time.sleep(0.5)
        check[4].click()
        time.sleep(0.5)
        check[5].click()
        time.sleep(0.5)
        check[6].click()
        time.sleep(0.5)
        check[7].click()
        time.sleep(0.5)
        check[8].click()
        time.sleep(1)
        self.driver.close()


    def test_Menu_Desplegable(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Canada']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'United Kingdom']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Germany']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'France']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Australia']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Japan']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'China']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'Brazil']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'India']").click()
        menu = self.driver.find_element(By.ID, "country")
        menu.find_element(By.XPATH, "//option[. = 'United States']").click()
        self.driver.close()


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


    def test_Web_Table(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='HTML1']/div[1]/table")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        tabla = self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
        for fila in tabla:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            datos_fila = [celda.text for celda in celdas if celda.text]
            if datos_fila:
                print("")
                print(datos_fila)

        print("")
        print("")

        tabla = self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
        for fila in tabla:
            celdas_encabezado = fila.find_elements(By.TAG_NAME, "th")
            if celdas_encabezado:
                datos_fila = [celda.text for celda in celdas_encabezado if celda.text.strip()]
                print("")
                print("Encabezado:", datos_fila)
            else:
                celdas_datos = fila.find_elements(By.TAG_NAME, "td")
                datos_fila = [celda.text for celda in celdas_datos if celda.text.strip()]
                print("")
                print("Datos de fila:", datos_fila)

        datos_esperados = ["Learn Selenium", "Learn Java", "Master In Selenium"]
        datos_tabla = [celda.text for fila in tabla for celda in fila.find_elements(By.TAG_NAME, "td")]
        for dato in datos_esperados:
            assert dato in datos_tabla, f"{dato} no encontrado en la tabla"
        print("")
        print("Todos los datos esperados están presentes.")
        self.driver.close()


    def test_Pagination_Table(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) input").click()
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.LINK_TEXT, "3").click()
        self.driver.find_element(By.LINK_TEXT, "4").click()
        self.driver.find_element(By.LINK_TEXT, "1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(3)").text == "$10.99"
        assert self.driver.find_element(By.CSS_SELECTOR,"tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)").text == "Product 4"
        self.driver.close()


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
        
        
    def test_resizable(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        boton_resize = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ui-icon-gripsmall-diagonal-se')))
        ActionChains(self.driver) \
            .move_to_element(boton_resize) \
            .click_and_hold(boton_resize) \
            .move_by_offset(-10, -10) \
            .release() \
            .perform()
        self.driver.close()


    def test_slider(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.ID, "cookieChoiceDismiss").click()
        except:
            pass
        self.driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "slider")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "slider")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "slider")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "slider")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle").click()
        self.driver.close()


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
