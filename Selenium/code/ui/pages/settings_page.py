from Selenium.code.ui.pages.base_page import BasePage
from Selenium.code.ui.locators.park_vk_locators import SettingsLocators


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = SettingsLocators()

    def fill_about_input(self, value):
        about_field = self.find(self.locators.ABOUT_INPUT)
        about_field.clear()
        about_field.send_keys(value)

    def submit(self):
        self.click(self.locators.SUBMIT_BTN)

    def update_about_input(self, value):
        self.fill_about_input(value)
        self.submit()

    def get_about_value(self):
        return self.find(self.locators.ABOUT_INPUT).text
