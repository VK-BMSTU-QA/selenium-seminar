import pytest

from base import BaseCase
from ui.pages.main_page import MainPage, MenuItem


class TestMainPage(BaseCase):

    @pytest.mark.parametrize(
        'start_menu_item,next_menu_item',
        [(MainPage.menu_item_blog, MainPage.menu_item_people),
         (MainPage.menu_item_program, MainPage.menu_item_alumni)])
    def test_menu_items(self, main_page: MainPage, start_menu_item: MenuItem,
                        next_menu_item: MenuItem):

        main_page.go_to_menu_item(start_menu_item['name'],
                                  start_menu_item['url'])
        main_page.go_to_menu_item(next_menu_item['name'],
                                  next_menu_item['url'])
