from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = basic_locators.SettingsPageLocators()

    def edit_about(self, text):
        self.fill(self.locators.ABOUT_INPUT, text)
        self.click(self.locators.SAVE_BTN)

    def get_about(self):
        return self.find(self.locators.ABOUT_INPUT).text
