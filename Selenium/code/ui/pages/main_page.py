from selenium.webdriver.common.by import By
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = basic_locators.MainPageLocators()

    def go_to_tab(self, tab_name):
        self.click((By.LINK_TEXT, tab_name))

    def get_active_tab(self):
        return self.find(self.locators.ACTIVE_TAB).text
