import time
from selenium.webdriver.common.by import By
from Assignment.Details import detail
from Assignment.Webbrowsers import webrowsers
class login(webrowsers,detail):
    def logintestcase(self,Browser):
        credentials=obj.webbrowser(Browser)
        credentials.find_element(by=By.CSS_SELECTOR, value='span[id="nav-link-accountList-nav-line-1"]').click()
        time.sleep(2)
        credentials.find_element(by=By.CSS_SELECTOR,value='input[id="ap_email"]').send_keys(obj.usernamedetails()[0])
        time.sleep(2)
        credentials.find_element(by=By.XPATH,value="//*[@tabindex=5]").click()
        credentials.find_element(by=By.XPATH,value="//*[@type='password']").send_keys(obj.password()[0])
        credentials.find_element(by=By.XPATH,value="//*[@id='signInSubmit']").click()
        time.sleep(3)

obj=login()
obj.logintestcase('Chrome')