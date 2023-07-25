import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        # Menggunakan driver yang telah didownload
        chromepath = "./chromedriver.exe"
        service = ChromeService(executable_path='./chromedriver.exe')
        self.browser = webdriver.Chrome(service=service)
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") # buka situs
        time.sleep(2)
        browser.find_element(By.ID, "txt-username").send_keys("John Doe"); # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "btn-login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        element_exist = browser.find_element(By.ID, "btn-book-appointment")
        current_url = browser.current_url

        self.assertTrue(element_exist)
        self.assertEqual(current_url, "https://katalon-demo-cura.herokuapp.com/#appointment")

    def test_a_failed_login_with_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") # buka situs
        time.sleep(2)
        browser.find_element(By.ID, "txt-username").send_keys("John Doe"); # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txt-password").send_keys("ThisIsAPassword") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "btn-login").click() # klik tombol sign in
        time.sleep(1)
        # validasi
        error_displayed = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").is_displayed
        self.assertTrue(error_displayed)

        error_text = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").text
        self.assertEqual(error_text, "Login failed! Please ensure the username and password are valid.")

    def test_a_failed_login_with_wrong_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") # buka situs
        time.sleep(2)
        browser.find_element(By.ID, "txt-username").send_keys("John Thor"); # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "btn-login").click() # klik tombol sign in
        time.sleep(1)
        # validasi
        error_displayed = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").is_displayed
        self.assertTrue(error_displayed)

        error_text = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").text
        self.assertEqual(error_text, "Login failed! Please ensure the username and password are valid.")

    def test_a_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") # buka situs
        time.sleep(2)
        browser.find_element(By.ID, "txt-username").send_keys(""); # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txt-password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "btn-login").click() # klik tombol sign in
        time.sleep(1)
        # validasi
        error_displayed = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").is_displayed
        self.assertTrue(error_displayed)

        error_text = browser.find_element(By.XPATH, "//*[@id='login']/div/div/div[1]/p[2]").text
        self.assertEqual(error_text, "Login failed! Please ensure the username and password are valid.")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()