import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    @allure.step('Get menu item')
    def get_menu_item(self, menu_item_name: str) -> WebElement:
        return self.find((By.LINK_TEXT, menu_item_name))

    @allure.step('Go to menu item')
    def go_to_menu_item(self, menu_item_name: str,
                        menu_item_url: str) -> EventsPage:
        self.get_menu_item(menu_item_name).click()
        return EventsPage(self.driver, menu_item_url)
