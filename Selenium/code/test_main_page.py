import pytest
from base import BaseCase

from ui.pages.main_page import MainPage


class TestMainPage(BaseCase):

    @pytest.mark.parametrize('first_menu_item,second_menu_item',
                             [(("Блоги", "blog/"), ("Люди", "people/")),
                              (("Программа", "curriculum/program/mine/"),
                               ("Выпуски", "alumni/"))])
    def test_menu_items(self, main_page: MainPage, first_menu_item,
                        second_menu_item):

        main_page.go_to_menu_item(*first_menu_item)
        main_page.go_to_menu_item(*second_menu_item)
