import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import login
from data import Data_CRUD

class Read_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_readdata_success(self):    
        driver = self.driver
        login.testLogin_success(driver)
        driver.find_element(By.ID, "searching").send_keys(Data_CRUD.path_email)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > form > input.btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > a.btn.btn-outline-info").click()
        time.sleep(1)
        result_email=driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dd:nth-child(12)").text
        self.assertEqual(result_email,Data_CRUD.path_email)

if __name__ == '__main__':
    unittest.main()
