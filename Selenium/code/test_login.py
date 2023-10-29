from base import BaseCase
from ui.fixtures import *
from ui.pages.login_page import LoginPage
from ui.pages.settings_page import SettingsPage


class TestLogin(BaseCase):
    authorize = False

    @allure.story('Login')
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        email, password = credentials
        main_page = login_page.login(email, password)
        assert main_page.is_opened()


class TestLK(BaseCase):

    @allure.story('Move to section')
    @pytest.mark.parametrize(
        'to_section, url',
        [
            pytest.param(
                'Люди', 'https://park.vk.company/people/'
            ),
            pytest.param(
                'Программа', 'https://park.vk.company/curriculum/program/mine/'
            )
        ]
    )
    def test_move_to(self, to_section, url):
        feed_page = FeedPage(self.driver)
        feed_page.move_to(to_section)

        assert self.driver.current_url.startswith(url)

    @allure.story('Edit bio')
    def test_edit_bio(self):
        feed_page = FeedPage(self.driver)
        feed_page.move_to_settings()
        settings_page = SettingsPage(self.driver)

        assert settings_page.is_opened()

        expected = 'hello world'
        settings_page.edit_bio('hello world')
        self.driver.refresh()
        actual = settings_page.get_bio()

        assert expected == actual
