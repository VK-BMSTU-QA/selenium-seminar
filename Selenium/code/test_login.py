from base import BaseCase, cookies, credentials
from ui.pages.base_page import PageNotOpenedExeption
import pytest


@pytest.fixture(scope='session')
def invalid_credentials():
    return ['login', 'password']


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(*credentials)

    def test_login_invalid(self, invalid_credentials):
        with pytest.raises(PageNotOpenedExeption):
            self.login_page.login(*invalid_credentials)
        self.login_page.has_error()
