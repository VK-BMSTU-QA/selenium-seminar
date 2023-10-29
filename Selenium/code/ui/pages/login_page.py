from Selenium.code.ui.pages.base_page import BasePage
from Selenium.code.ui.locators.park_vk_locators import LoginLocators
from Selenium.code.ui.pages.main_page import MainPage

from Selenium.code.ui.pages.base_page import PageNotOpenedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    authorize = False

    locators = LoginLocators()

    def login(self, user, password):
        self.click(self.locators.BTN_LOCATOR)

        login_input = self.find_visible(self.locators.INPUT_LOGIN)
        password_input = self.find_visible(self.locators.INPUT_PASSWORD)

        login_input.send_keys(user)
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BTN)

        return MainPage(self.driver)

    def check_for_errors(self):
        self.find(self.locators.ERROR_MESSAGE)
