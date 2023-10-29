import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from ui.fixtures import get_driver
import json


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            for cookie in request.getfixturevalue('cookies'):
                self.driver.add_cookie(cookie)
            self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
        
        with open('files/creds.json') as cred_file:
            creds_object = json.load(cred_file)
        return {
             'login': creds_object['login'],
             'password': creds_object['pass']
        }

@pytest.fixture(scope='session')
def false_credentials():
     return {
          'login':'admin',
          'password':'admin'
     }

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])

    login_page = LoginPage(driver)
    login_page.login(credentials['login'], credentials['password'])
    session_cookies = driver.get_cookies
    driver.quit()
    return session_cookies
