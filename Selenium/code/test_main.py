import pytest

from test_login import BaseCase


class TestMain(BaseCase):
    @staticmethod
    def check_go_to_tab(main_page, tab_name, tab_url):
        main_page.go_to_tab(tab_name)
        main_page.check_url(tab_url)

    @pytest.mark.parametrize(
        'first_tab,second_tab',
        [
            pytest.param(
                ('Блоги', 'https://park.vk.company/blog/'), ('Люди', 'https://park.vk.company/people/')
            ),
            pytest.param(
                ('Программа', 'https://park.vk.company/curriculum/program/mine/'),
                ('Выпуски', 'https://park.vk.company/alumni/')
            ),
        ]
    )
    def test_two_tab_going(self, vk_main_page, first_tab, second_tab):
        self.check_go_to_tab(vk_main_page, first_tab[0], first_tab[1])
        self.check_go_to_tab(vk_main_page, second_tab[0], second_tab[1])
