import pytest
from _pytest.fixtures import FixtureRequest
# from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            for cookie in request.getfixturevalue('cookies'):
                driver.add_cookie(cookie)
            driver.refresh()

            print('Do something for login')
