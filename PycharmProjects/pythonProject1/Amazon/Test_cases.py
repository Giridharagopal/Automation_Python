import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.usefixtures("web")
class Test_Amazon():
    def test_entirecases(self):
        # self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.find_element(by=By.XPATH,value='//input[@id="twotabsearchtextbox"]').send_keys("mouse")
        self.driver.find_element(by=By.XPATH, value='//input[@id="nav-search-submit-button"]').click()