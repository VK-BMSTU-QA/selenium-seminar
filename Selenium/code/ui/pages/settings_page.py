from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = basic_locators.SettingsLocators

    def get_bio(self):
        result = self.find(self.locators.BIO_LOCATOR)
        return result.get_attribute('value')

    def edit_bio(self, new_bio):
        self.fill_field(self.locators.BIO_LOCATOR, new_bio)
        self.click(self.locators.SETTING_SUBMIT_LOCATOR)
