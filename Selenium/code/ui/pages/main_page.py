from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = basic_locators.MainPageLocators()

    def get_tab(self, tab_name) -> WebElement:
        return self.find((By.LINK_TEXT, tab_name))

    def go_to_tab(self, tab_name):
        self.click((By.LINK_TEXT, tab_name))
