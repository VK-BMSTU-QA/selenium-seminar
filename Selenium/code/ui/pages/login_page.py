from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    authorize = False

    locators = basic_locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.locators.LOGIN)

        self.fill_input(self.locators.USER, user)
        self.fill_input(self.locators.PASSWORD, password)

        self.click(self.locators.SUBMIT_LOGIN)

        return MainPage(self.driver)
