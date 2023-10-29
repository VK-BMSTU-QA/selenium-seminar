import pytest
from base import BaseCase

class TestMainSwitchTabs(BaseCase):
    authorize = True

    @pytest.mark.parametrize('tab_1, tab_2, expected_url', [
        ("BLOGS", "PEOPLE", 'https://park.vk.company/people/'),
        ("PROGRAMS", "PEOPLE_RELEASES", 'https://park.vk.company/alumni/')
    ])
    def test_switch_tab(self, tab_1, tab_2, expected_url, main_page, cookies):
        self.main_page.go_to_tab(tab_1)
        self.main_page.go_to_tab(tab_2)

        assert self.driver.current_url == expected_url


        