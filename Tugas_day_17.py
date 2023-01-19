import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def testlogin1_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

    def testlogin2_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

    def testlogin3_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

    def testlogin4_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

    def testlogin5_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("tandard_user") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        
unittest.main()