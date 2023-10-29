import pytest

from base import BaseCase
from ui.pages.base_page import PageNotOpenedExeption
from ui.pages.login_page import LoginPage


class TestLogin(BaseCase):
    authorize = False

    def test_login_success(self, login_page: LoginPage, credentials):
        login_page.login(**credentials)

    def test_login_wrong_user(self, login_page: LoginPage, credentials):
        with pytest.raises(PageNotOpenedExeption):
            login_page.login('wrong_user@mail.ru', credentials['password'])

        assert login_page.has_errors()

    def test_login_wrong_password(self, login_page: LoginPage, credentials):
        with pytest.raises(PageNotOpenedExeption):
            login_page.login(credentials['user'], 'wrong_password')

        assert login_page.has_errors()
