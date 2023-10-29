import pytest
from base import BaseCase
from ui.locators.basic_locators import MainPageLocators

class TestMainSwitchTabs(BaseCase):
    authorize = True
    locators = MainPageLocators()

    @pytest.mark.parametrize('tab_1, tab_2, expected_url', [
        (locators.BLOGS, locators.PEOPLE, 'https://park.vk.company/people/'),
        (locators.PROGRAM, locators.PEOPLE_RELEASES, 'https://park.vk.company/alumni/')
    ])
    def test_switch_tab(self, tab_1, tab_2, expected_url, main_page, cookies):
        self.main_page.go_to_tab(tab_1)
        self.main_page.go_to_tab(tab_2)

        assert self.driver.current_url == expected_url


        