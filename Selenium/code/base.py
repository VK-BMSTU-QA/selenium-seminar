from contextlib import contextmanager
import json

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.login_page import LoginPage
from ui.fixtures import get_driver


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page: LoginPage = LoginPage(driver)

        if self.authorize:
            for cookie in request.getfixturevalue('cookies'):
                self.driver.add_cookie(cookie)

            self.driver.refresh()

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(config['url'])

    LoginPage(driver).login(credentials["user"], credentials["password"])
    cookies = driver.get_cookies()

    driver.quit()
    return cookies


@pytest.fixture(scope='session')
def credentials():
    with open('cred.json') as f:
        return json.load(f)

