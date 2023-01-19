import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class DashboardNavbar_kelompok_15(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Check can aaccess the website
    def testDashboardNavbar(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")  # open the website
        driver.maximize_window()
        time.sleep(2)
    
        # Navigation Bar
        # Logo
        driver.find_element(By.CSS_SELECTOR, "img[alt='Itera logo']").click()
        time.sleep(2)
        
        # Home
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click()
        time.sleep(2)

        # Practice
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/home/practice']").click()
        time.sleep(2)

        # Test Automation
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/home/automation']").click()
        time.sleep(2)

        # Tutorial
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/home/tutorial']").click()
        time.sleep(2)

        # Sign Up
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click()
        time.sleep(2)

        # Login
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/form[@class='form-inline my-2 my-lg-0']//a[@href='/Login']").click()
        time.sleep(2)

        # Search
        # Fill with string
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.CSS_SELECTOR, ".form-control.mr-sm-2").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(5)

        # Fill with number
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.CSS_SELECTOR, ".form-control.mr-sm-2").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()