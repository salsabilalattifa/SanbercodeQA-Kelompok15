import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import login
from data import Data_create

class Create_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_invalid_phone(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > p:nth-child(4) > a").click()
        time.sleep(1)

        driver.find_element(By.ID, "Name").send_keys(Data_create.valid_name)
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys(Data_create.valid_company)
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys(Data_create.valid_adress)
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys(Data_create.valid_city)
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys(Data_create.invalid_phone)
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys(Data_create.valid_email)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(9) > div > input").click()


    def test_create_invalid_email(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > p:nth-child(4) > a").click()
        time.sleep(1)

        driver.find_element(By.ID, "Name").send_keys(Data_create.valid_name)
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys(Data_create.valid_company)
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys(Data_create.valid_adress)
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys(Data_create.valid_city)
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys(Data_create.valid_phone)
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys(Data_create.invalid_email)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(9) > div > input").click()

    def test_create_jmpty_data(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > p:nth-child(4) > a").click()
        time.sleep(1)

        driver.find_element(By.ID, "Name").send_keys(Data_create.empty_name)
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys(Data_create.empty_company)
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys(Data_create.empty_adress)
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys(Data_create.empty_city)
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys(Data_create.empty_phone)
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys(Data_create.empty_email)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(9) > div > input").click()

    def test_success_create(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > p:nth-child(4) > a").click()
        time.sleep(1)

        driver.find_element(By.ID, "Name").send_keys(Data_create.valid_name)
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys(Data_create.valid_company)
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys(Data_create.valid_adress)
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys(Data_create.valid_city)
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys(Data_create.valid_phone)
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys(Data_create.valid_email)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(9) > div > input").click()
        time.sleep(1)
        driver.find_element(By.ID, "searching").send_keys(Data_create.valid_name)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        
        result=driver.find_element(By.CSS_SELECTOR,"body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").text
        self.assertEqual(result,Data_create.valid_name)

        

if __name__ == '__main__':
    unittest.main()