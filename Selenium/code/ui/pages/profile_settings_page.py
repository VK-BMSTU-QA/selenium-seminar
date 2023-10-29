import allure

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class ProfileSettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = basic_locators.ProfileSettingsPageLocators()

    @allure.step('Change about')
    def change_about(self, new_about: str):
        about = self.find(self.locators.ABOUT)
        about.clear()
        about.send_keys(new_about)
        self.click(self.locators.SUBMIT_FORM)

    @allure.step('Get about')
    def get_about(self):
        return self.find(self.locators.ABOUT).text
