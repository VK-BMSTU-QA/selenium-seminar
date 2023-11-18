from typing import TypedDict

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage


class MenuItem(TypedDict):
    name: str
    url: str


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    menu_item_blog: MenuItem = {'name': 'Блоги', 'url': 'blog/'}
    menu_item_people: MenuItem = {'name': 'Люди', 'url': 'people/'}
    menu_item_program: MenuItem = {
        'name': 'Программа',
        'url': 'curriculum/program/mine/'
    }
    menu_item_alumni: MenuItem = {'name': 'Выпуски', 'url': 'alumni/'}

    @allure.step('Get menu item')
    def get_menu_item(self, menu_item_name: str) -> WebElement:
        return self.find((By.LINK_TEXT, menu_item_name))

    @allure.step('Go to menu item')
    def go_to_menu_item(self, menu_item_name: str,
                        menu_item_url: str) -> EventsPage:
        self.get_menu_item(menu_item_name).click()
        return EventsPage(self.driver, menu_item_url)
