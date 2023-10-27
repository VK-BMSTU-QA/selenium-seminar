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

        tab = main_page.get_tab(tab_name)
        tab_class = tab.find_element(
            *BasePageLocators.PARENT).get_dom_attribute('class')
        assert 'active' in tab_class

    @pytest.mark.parametrize('first_tab,second_tab', tabs_data)
    def test_tabs(self, main_page, first_tab, second_tab):
        self.go_to_tab(main_page, *first_tab)
        self.go_to_tab(main_page, *second_tab)
