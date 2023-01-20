import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def testLogin_success(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("gaergarga")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("password8")
        time.sleep(1)
        driver.find_element(By.NAME, "clear").click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()