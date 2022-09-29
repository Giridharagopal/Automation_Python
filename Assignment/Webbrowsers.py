from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class webrowsers():
    def webbrowser(self,Browser,web=None):
        if Browser=="Chrome":
            driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
            driver.get("https://www.amazon.in/")
            return driver
        elif Browser=="Microsoft ":
            driver1=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=web)
            driver1.get("https://www.google.com/")
            return driver1
        elif Browser=="Firefox":
            driver2=webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=web)
            driver2.get("https://www.google.com/")
            return driver2



#obj=webrowsers()
#obj.webbrowser('Microsoft')