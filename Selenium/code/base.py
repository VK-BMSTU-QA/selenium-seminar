from contextlib import contextmanager
import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.login_page import LoginPage
import json


class BaseCase:
    driver = None
    authorize = False

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest): # request - инфа о тесте, который запрашивает фикстуру
        self.driver = driver
        self.config = config

        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
        self.settings_page: SettingsPage = (request.getfixturevalue('settings_page'))

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
    return json.load('files/creds.json')

@pytest.fixture(scope='session')
def cookies(credentials, login_page: LoginPage):
    login_page.login(credentials)
    return login_page.driver.get_cookies()
