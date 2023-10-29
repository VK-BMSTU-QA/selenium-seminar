from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage
from selenium.webdriver.support.ui import Select


class ProfilePage(BasePage):
    locators = basic_locators.ProfileLocators()
    url = 'https://park.vk.company/cabinet/settings/'
    name_of_page = "Profile"

    @allure.step('Change cloth size')
    def change_size(self, new_size, timeout = 5):
        clothes_select = self.find(self.locators.CLOTHES_LOCATOR, timeout)
        select = Select(clothes_select)
        select.select_by_value(new_size)

        self.click(self.locators.SAVE_LOCATOR)

    @allure.step('Clear size')
    def clear_size(self):
        self.change_size("")

    @allure.step('Clear size')
    def get_current_size(self):
        selector = Select(self.find(self.locators.CLOTHES_LOCATOR))
        return selector.first_selected_option.get_attribute("value")

    def change_about(self, text):
        text_input = self.find(self.locators.ABOUT_LOCATOR)
        text_input.clear()

        text_input.send_keys(text)
    
    def get_about_info(self):
        about_field = self.find(self.locators.ABOUT_LOCATOR)
        return about_field.get_attribute("value")

