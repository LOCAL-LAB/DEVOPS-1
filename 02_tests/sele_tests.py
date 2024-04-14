import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class SearchProductTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def test_search(self):
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        search_box = driver.find_element(By.NAME,'q')
        search_box.send_keys("two cities")
        search_button = driver.find_element(By.CLASS_NAME,'search-button')
        search_button.click()
        driver.save_screenshot("zdjecie1.png")
    
    def tearDown(self):
        self.driver.quit()