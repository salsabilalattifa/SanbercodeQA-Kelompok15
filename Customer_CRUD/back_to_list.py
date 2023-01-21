import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import login

class Backtolist_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_back_to_list(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > p:nth-child(4) > a").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > a").click()
        time.sleep(1)

        driver.get("https://itera-qa.azurewebsites.net/Dashboard")

    def test_update_back_to_list(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > a.btn.btn-outline-primary").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > a").click()
        time.sleep(1)  

        driver.get("https://itera-qa.azurewebsites.net/Dashboard")

    def test_delete_back_to_list(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > a.btn.btn-outline-danger").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > div > a").click()
        time.sleep(1) 

        driver.get("https://itera-qa.azurewebsites.net/Dashboard")

    def test_read_back_to_list(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > a.btn.btn-outline-info").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > p > a.btn.btn-link").click()
        time.sleep(1)               

        driver.get("https://itera-qa.azurewebsites.net/Dashboard")

if __name__ == '__main__':
    unittest.main()        