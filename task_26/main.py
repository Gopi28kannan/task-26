from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Data import data
from Locators import locators
import pytest

class Test_Webpage:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_open_webpage(self):
        self.driver.get(data.web_data().url)
        self.driver.maximize_window()

    def test_fill_form(self):
        
        #include explicit wait
        wait = WebDriverWait(self.driver, 20)
        #expand all button is not a clickable button, so use script method
        expand = wait.until(EC.presence_of_element_located((By.XPATH, locators.web_locators().expand_all)))
        self.driver.execute_script("arguments[0].click();", expand)
        #send name
        wait.until(EC.presence_of_element_located((By.ID, locators.web_locators().name))).send_keys(data.web_data().name)
        #send from birth
        wait.until(EC.presence_of_element_located((By.ID, locators.web_locators().from_birth))).send_keys(data.web_data().from_birth)
        #send to birth
        wait.until(EC.presence_of_element_located((By.ID, locators.web_locators().to_birth))).send_keys(data.web_data().to_birth)
        #send birthday
        wait.until(EC.presence_of_element_located((By.ID, locators.web_locators().birthday))).send_keys(data.web_data().birthday)
        #click page topic and this is not a clickable button so use script method
        page_topic = wait.until(EC.presence_of_element_located((By.XPATH, locators.web_locators().page_of_topic)))
        self.driver.execute_script("arguments[0].click();", page_topic)
        #and same gender not a clickable button
        Gender = wait.until(EC.presence_of_element_located((By.XPATH, locators.web_locators().gender)))
        self.driver.execute_script("arguments[0].click();", Gender)
        #and last then click see result button
        click_see_result = wait.until(EC.presence_of_element_located((By.XPATH, locators.web_locators().see_result)))
        self.driver.execute_script("arguments[0].click();", click_see_result)
        print("result successfully captured")
        
