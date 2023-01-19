import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # LOGIN TEST CASE
    def testLogin_failed(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("inisalah")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("123456")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    def testLogin_wrong_password(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("admin")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("123456")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    def testLogin_wrong_username(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("inisalah")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("admin")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    def testLogin_failed_blank(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    def testLogin_success(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login/Index/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("admin")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "Password").send_keys("admin")
        time.sleep(1)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()