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


