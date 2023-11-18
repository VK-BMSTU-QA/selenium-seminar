from base import BaseCase, cookies, credentials
from ui.locators.basic_locators import BasePageLocators
from ui.fixtures import main_page
import pytest


tabs_data = [
    (('Люди', 'people/'), ('Блоги', 'blog/')),
    (('Программа', 'curriculum/program/mine/'), ('Выпуски', 'alumni/')),
]


class TestMainPage(BaseCase):
    def go_to_tab(self, main_page, tab_name, tab_url):
        main_page.go_to_tab(tab_name)
        main_page.check_url(f'https://park.vk.company/{tab_url}')
        assert tab_name == main_page.get_active_tab()

    @pytest.mark.parametrize('initial_tab,next_tab', tabs_data)
    def test_tabs(self, main_page, initial_tab, next_tab):
        self.go_to_tab(main_page, *initial_tab)
        self.go_to_tab(main_page, *next_tab)
