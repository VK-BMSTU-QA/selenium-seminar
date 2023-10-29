from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.login_page import LoginPage
from ui.fixtures import get_driver

CLICK_RETRY = 3


class BaseCase:
    driver = None
    authorize = True

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
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
    with open('files/credentials.txt', 'r') as file:
        login, password = file.readline().split(':')
        return login, password


@pytest.fixture(scope='session')
def invalid_credentials():
    return ['invalid_login', 'invalid_password']


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    url = config['url']

    driver.get(url)

    LoginPage(driver).login(*credentials)
    cookies = driver.get_cookies()

    driver.quit()

    return cookies
