from selenium.webdriver.common.by import By
import time


class MainPageElements():
    def __init__(self, driver):
        self.driver = driver

    def mainPageLogo(self):
        logo = self.driver.find_element(By.CLASS_NAME, 'page-header__logo')
        logo.click()

    #
    # def headerButtons(self):
    #     buttons_list = self.driver.find_elements(By.XPATH, "//li[@class='sitenav-item']/a")
    #     length_of_buttons = len(buttons_list)
    #
    #     for element in range(length_of_buttons):
    #         if not buttons_list[element].is_displayed():
    #             time.sleep(2)
    #             self.driverBack()
    #
    #
    #         buttons_list[element].click()
    #         buttons_list = self.driver.find_elements(By.XPATH, "//li[@class='sitenav-item']/a")

###########_______---------------______---__-_-_-_-_-_-_-_-_-_-


    def headerButtons1(self):
        buttons_list = self.driver.find_elements(By.XPATH, "//li[@class='sitenav-item']/a")
        length_of_buttons = len(buttons_list)

        for element in range(length_of_buttons):
            buttons_list[element].click()

            self.driverBack()
            time.sleep(2)

            buttons_list = self.driver.find_elements(By.XPATH, "//li[@class='sitenav-item']/a")

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