from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.vk_main_page import VKMainPage


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    locators = basic_locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.locators.LOGIN_BTN)

        self.fill(self.locators.LOGIN_FIELD, user)
        self.fill(self.locators.PASSWD_FIELD, password)

        self.click(self.locators.SUBMIT_LOGIN_BTN)

        return VKMainPage(self.driver)

    def error_msg(self):
        return self.find(self.locators.ERR_MSG).text
