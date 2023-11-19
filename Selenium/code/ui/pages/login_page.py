from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.feed_page import FeedPage


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    locators = basic_locators.LoginPageLocators

    def login(self, email, password):
        self.logger.debug("Starting authorization")

        self.click(self.locators.TRIGGER_LOGIN_LOCATOR)
        self.fill_field(self.locators.EMAIL_LOCATOR, email)
        self.fill_field(self.locators.PASSWORD_LOCATOR, password)
        self.click(self.locators.ENTER_LOGIN_LOCATOR)

        self.logger.debug("Authorization data has been successfully entered")

        return FeedPage(self.driver)
