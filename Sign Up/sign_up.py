import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Register_kelompok_15(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # REGISTER TEST CASE
    def test_Register_success(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi firstname
        driver.find_element(By.ID, "FirstName").send_keys("Erga")
        time.sleep(1)
        # isi surname
        driver.find_element(By.ID, "Surname").send_keys("Saputra")
        time.sleep(1)
        # isi e-post
        driver.find_element(By.ID, "E_post").send_keys("saputraerga26@gmail.com")
        time.sleep(1)
        # isi mobile
        driver.find_element(By.ID, "Mobile").send_keys("087883415795")
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("gaergarga")
        time.sleep(1)
        # isi password
        driver.find_element(By.ID, "Password").send_keys("password8")
        time.sleep(1)
        # isi confirm password
        driver.find_element(By.ID, "ConfirmPassword").send_keys("password8")
        time.sleep(1)
        # click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

    def test_Register_failed_using_registered_account(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi firstname
        driver.find_element(By.ID, "FirstName").send_keys("Erga")
        time.sleep(1)
        # isi surname
        driver.find_element(By.ID, "Surname").send_keys("Saputra")
        time.sleep(1)
        # isi e-post
        driver.find_element(By.ID, "E_post").send_keys("saputraerga26@gmail.com")
        time.sleep(1)
        # isi mobile
        driver.find_element(By.ID, "Mobile").send_keys("087883415795")
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("gaergarga")
        time.sleep(1)
        # isi password
        driver.find_element(By.ID, "Password").send_keys("password8")
        time.sleep(1)
        # isi confirm password
        driver.find_element(By.ID, "ConfirmPassword").send_keys("password8")
        time.sleep(1)
        # click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
    
    def test_Register_failed_blank_field(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi firstname
        driver.find_element(By.ID, "FirstName").click()
        time.sleep(1)
        # isi surname
        driver.find_element(By.ID, "Surname").click()
        time.sleep(1)
        # isi e-post
        driver.find_element(By.ID, "E_post").click()
        time.sleep(1)
        # isi mobile
        driver.find_element(By.ID, "Mobile").click()
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").click()
        time.sleep(1)
        # isi password
        driver.find_element(By.ID, "Password").click()
        time.sleep(1)
        # isi confirm password
        driver.find_element(By.ID, "ConfirmPassword").click()
        time.sleep(1)
        # click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

    def test_Register_failed_unmatch_password(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi firstname
        driver.find_element(By.ID, "FirstName").send_keys("Erga")
        time.sleep(1)
        # isi surname
        driver.find_element(By.ID, "Surname").send_keys("Saputra")
        time.sleep(1)
        # isi e-post
        driver.find_element(By.ID, "E_post").send_keys("saputraerga26@gmail.com")
        time.sleep(1)
        # isi mobile
        driver.find_element(By.ID, "Mobile").send_keys("087883415795")
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("gaergarga")
        time.sleep(1)
        # isi password
        driver.find_element(By.ID, "Password").send_keys("password8")
        time.sleep(1)
        # isi confirm password
        driver.find_element(By.ID, "ConfirmPassword").send_keys("password")
        time.sleep(1)
        # click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

    def test_Register_failed_invalid_email_address(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi firstname
        driver.find_element(By.ID, "FirstName").send_keys("test email")
        time.sleep(1)
        # isi surname
        driver.find_element(By.ID, "Surname").send_keys("est email")
        time.sleep(1)
        # isi e-post
        driver.find_element(By.ID, "E_post").send_keys("testmail")
        time.sleep(1)
        # isi mobile
        driver.find_element(By.ID, "Mobile").send_keys("5678765678")
        time.sleep(1)
        # isi username
        driver.find_element(By.ID, "Username").send_keys("monysachi")
        time.sleep(1)
        # isi password
        driver.find_element(By.ID, "Password").send_keys("123")
        time.sleep(1)
        # isi confirm password
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123")
        time.sleep(1)
        # click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()