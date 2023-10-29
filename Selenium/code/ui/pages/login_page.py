import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import MainPage

class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators()
    url = 'https://park.vk.company/'

    @allure.step("Login")
    def login(self, creds, timeout=5):
        self.click(self.locators.LOGIN_BTN_MAIN_SCREEN, timeout)
        self.fill(self.locators.EMAIL_INPUT, creds["email"], timeout)
        self.fill(self.locators.PASS_INPUT, creds["password"], timeout)
        self.click(self.locators.LOGIN_BTN_FORM, timeout)
        return MainPage(self.driver)
