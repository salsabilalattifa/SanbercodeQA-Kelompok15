import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import login
from data import Data_CRUD

class Update_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_update_invalid_phone(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.find_element(By.ID, "searching").send_keys(Data_CRUD.path_email)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"Phone").clear()
        time.sleep(1)
        driver.find_element(By.ID,"Phone").send_keys(Data_CRUD.invalid_phone)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()

    def test_update_invalid_email(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.find_element(By.ID, "searching").send_keys(Data_CRUD.update_email_invalid)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"Email").clear()
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys(Data_CRUD.invalid_email)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()

    def test_update_empty_data(self):
        driver = self.driver
        login.testLogin_success(driver)
        driver.find_element(By.ID, "searching").send_keys(Data_CRUD.path_email)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "Name").clear()
        time.sleep(1)
        driver.find_element(By.ID, "Company").clear()
        time.sleep(1)
        driver.find_element(By.ID, "Address").clear()
        time.sleep(1)
        driver.find_element(By.ID, "City").clear()
        time.sleep(1)
        driver.find_element(By.ID, "Phone").clear()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()    
        
    def test_update_success(self):    
        driver = self.driver
        login.testLogin_success(driver)
        driver.find_element(By.ID, "searching").send_keys(Data_CRUD.path_email)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"Name").clear()
        driver.find_element(By.ID, "Name").send_keys(Data_CRUD.valid_name)
        time.sleep(1)
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID, "Company").send_keys(Data_CRUD.valid_company)
        time.sleep(1)
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID, "Address").send_keys(Data_CRUD.valid_adress)
        time.sleep(1)
        driver.find_element(By.ID,"City").clear()
        driver.find_element(By.ID, "City").send_keys(Data_CRUD.valid_city)
        time.sleep(1)
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID, "Phone").send_keys(Data_CRUD.valid_phone)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()

if __name__ == '__main__':
    unittest.main()