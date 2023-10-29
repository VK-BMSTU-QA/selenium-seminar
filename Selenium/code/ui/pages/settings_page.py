from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    locators = basic_locators.SettingsPageLocators()

    def edit_about(self, contents):
        self.fill_in(self.locators.ABOUT, contents)
        self.click(self.locators.SUBMIT_PROFILE_EDIT)

    def about_contents(self):
        return self.find(self.locators.ABOUT).text

    def set_clothes_size(self, size):
        sizes = Select(self.find(self.locators.CLOTHES_SIZE))
        sizes.select_by_visible_text(size)
        self.click(self.locators.SUBMIT_PROFILE_EDIT)

    def clothes_size(self):
        sizes = Select(self.find(self.locators.CLOTHES_SIZE))
        return sizes.all_selected_options[0].text
