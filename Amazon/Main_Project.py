import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class workout():
    def testing(self, web=None):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://www.amazon.in/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH, value='//input[starts-with(@autocomplete,"off")]').send_keys("Reebookshoes")
        self.driver.find_element(by=By.ID, value="nav-search-submit-button").click()
        self.driver.find_element(by=By.XPATH, value="//*[@aria-label='Go to page 2']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value='''//*[@alt="Reebok Classics Men's Reebok Clubonic Sneaker" ]''').click()
        time.sleep(3)
        singledropdown=Select(self.driver.find_element(by=By.CSS_SELECTOR, value='select[name="dropdown_selected_size_name"]'))
        singledropdown.select_by_value( '6 UK')

        #self.driver.quit()
        #print("completed")
obj=workout()
obj.testing()