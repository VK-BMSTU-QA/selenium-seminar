import pytest

from base import BaseCase, cookies, credentials
from ui.locators.park_vk_locators import TabLocators


class TestTab(BaseCase):
    authorize = True

    tab_locators = TabLocators()

    tabs_test_data = [
        ('blog/', tab_locators.PEOPLE_TAB, 'people/'),
        ('feed/', tab_locators.BLOG_TAB, 'blog/'),
        ('blog/', tab_locators.PLAN_TAB, 'curriculum/program/mine/')
    ]

    @pytest.mark.parametrize('original_url,tab_locator,target_url', tabs_test_data)
    def test_tab_redirect(self, main_page, original_url, tab_locator, target_url):
        self.driver.get('https://park.vk.company/' + original_url)
        main_page.click(tab_locator)

        assert self.driver.current_url == 'https://park.vk.company/' + target_url
