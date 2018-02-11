from selenium.webdriver.common.by import By
import time


class MainPageElements():
    def __init__(self, driver):
        self.driver = driver

    def mainPageLogo(self):
        logo = self.driver.find_element(By.CLASS_NAME, 'page-header__logo')
        logo.click()

    def buttons(self):
        buttons_list = self.driver.find_elements(By.XPATH, "//ul[@class='sitenav']/li")
        for button in range(len(buttons_list)):
            buttons_list = self.driver.find_elements(By.XPATH, "//ul[@class='sitenav']/li")
            buttons_list[button].click()
            time.sleep(3)
            if len(self.driver.find_elements(By.XPATH, "//ul[@class='sitenav']")) < 1:
                print("Goind back " + "\n")
                self.driver.back()

    def whatsAppWeb(self):
        whatsapp_web = self.driver.find_element(By.XPATH, "//li[contains(text(),'Open')]")
        whatsapp_web.click()

    def features(self):
        features_btn = self.driver.find_element(By.CLASS_NAME, 'hero-phone')
        if features_btn is not None:
            return True
        else:
            return False

    def driverBack(self):
        self.driver.back()