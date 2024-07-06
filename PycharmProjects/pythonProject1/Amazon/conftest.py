import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def webs(self):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.amazon.in/")
    driver.maximize_window()


