from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    locators = basic_locators.SettingsPageLocators()

    def set_about(self, contents):
        self.fill_input(self.locators.ABOUT, contents)
        self.click(self.locators.SUBMIT_PROFILE_EDIT)

    def get_about(self):
        return self.find(self.locators.ABOUT).text
