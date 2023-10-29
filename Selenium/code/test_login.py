import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import PageNotOpenedExeption
from ui.pages.login_page import LoginPage


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

            driver.refresh()


@pytest.fixture(scope='session')
def wrong_credentials():
    return ['wronger', 'wrong_pswd']


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(credentials[0], credentials[1])

    def test_wrong_login(self, wrong_credentials):
        with pytest.raises(PageNotOpenedExeption):
            self.login_page.login(wrong_credentials[0], wrong_credentials[1])
        assert self.login_page.error_msg() == 'Учётные данные неверны'
