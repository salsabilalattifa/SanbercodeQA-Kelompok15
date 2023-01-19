import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class DashboardButtons_kelompok_15(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Check can aaccess the website
    def testDashboardButtons(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")  # open the website
        driver.maximize_window()
        time.sleep(2)

        # Button Read Me at Test Automation
        driver.find_element(By.XPATH, "/html/body/div[1]/div[@class='jumbotron']/p[2]/a[@href='#']").click()
        time.sleep(2)

        # Button Read Me at Selenium Webdriver
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.XPATH, "/html/body/div[1]/div[@class='row']/div[1]/p[2]/a[@href='#']").click()
        time.sleep(2)

        # Button Read Me at To Automate or Not to Automate?
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.XPATH, "/html/body/div[1]/div[@class='row']/div[2]/p[2]/a[@href='#']").click()
        time.sleep(2)

        # Button Read Me at Security testing
        driver.find_element(By.XPATH, "//nav/div[@class='collapse navbar-collapse']/ul//a[@href='/']").click() # go to home page
        driver.find_element(By.XPATH, "/html/body/div[1]/div[@class='row']/div[3]/p[2]/a[@href='#']").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()