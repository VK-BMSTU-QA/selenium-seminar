from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage
from selenium.webdriver.support.ui import Select


class ProfilePage(BasePage):
    locators = basic_locators.ProfileLocators()
    url = 'https://park.vk.company/cabinet/settings/'
    nameOfPage = "Profile"

    @allure.step('Change cloth size')
    def changeSize(self, newSize, timeout = 5):
        clothesSelect = self.find(self.locators.CLOTHES_LOCATOR, timeout)
        select = Select(clothesSelect)
        select.select_by_value(newSize)

        self.click(self.locators.SAVE_LOCATOR)

    @allure.step('Clear size')
    def clearSize(self):
        self.changeSize("")

    @allure.step('Clear size')
    def getCurrentSize(self):
        selector = Select(self.find(self.locators.CLOTHES_LOCATOR))
        return selector.first_selected_option.get_attribute("value")
