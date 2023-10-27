from base import BaseCase, cookies, credentials
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage
from ui.locators.basic_locators import BasePageLocators
import pytest


tabs_data = [
    (('Люди', 'people/'), ('Блоги', 'blog/')),
    (('Программа', 'curriculum/program/mine/'), ('Выпуски', 'alumni/')),
]


class TestMainPage(BaseCase):
    def go_to_tab(self, tab_name, tab_url):
        self.main_page.go_to_tab(tab_name)
        self.main_page.await_redirect(
            f'https://park.vk.company/{tab_url}')

        tab = self.main_page.get_tab(tab_name)
        tab_class = tab.find_element(
            *BasePageLocators.PARENT).get_dom_attribute('class')
        assert 'active' in tab_class

    @pytest.mark.parametrize('first_tab,second_tab', tabs_data)
    def test_tabs(self, first_tab, second_tab):
        self.main_page = MainPage(self.driver)

        self.go_to_tab(*first_tab)
        self.go_to_tab(*second_tab)
