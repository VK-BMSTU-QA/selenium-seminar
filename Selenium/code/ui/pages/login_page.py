from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.events_page import EventsPage
from selenium.webdriver.support.ui import Select

class LoginPage(BasePage):
    url = 'https://park.vk.company/pages/index/?next=/feed/#auth'
    locators = basic_locators.LoginLocators()
    nameOfPage = "Login"

    def writeToField(self, locator, dataToWrite):
        element = self.find(locator)
        element.clear()

        element.send_keys(dataToWrite)        
            
    def writeLoginAndPass(self, user, password):
        self.writeToField(self.locators.LOGIN_LOCATOR, user)
        self.writeToField(self.locators.PASSWORD_LOCATOR, password)

    def login(self, user, password):
        self.writeLoginAndPass(user, password)
        self.click(self.locators.LOGIN_BUTTON_LOCATOR)

        return self.driver