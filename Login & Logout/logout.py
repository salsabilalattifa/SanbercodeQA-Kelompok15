import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

     # LOGOUT TEST CASE
    def test_logout(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/")  # buka websitenya
        driver.maximize_window()
        time.sleep(2)
        # isi email
        driver.find_element(By.ID, "Username").send_keys("admin")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("admin")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()

if __name__ == '__main__':
    unittest.main()