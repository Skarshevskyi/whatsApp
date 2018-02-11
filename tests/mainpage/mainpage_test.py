from selenium import webdriver
from pages.mainpage.mainpage import MainPageElements
import unittest

class MainPage(unittest.TestCase):

    def test_header_buttons(self):
        baseUrl = "https://www.whatsapp.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        mp = MainPageElements(driver)


# -------test
        mp.mainPageLogo()
        mp.buttons()

# if __name__ == '__main__':
#     MainPage().test_header_buttons()

