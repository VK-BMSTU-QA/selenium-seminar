from base import BaseCase, cookies, credentials
from ui.pages.base_page import PageNotOpenedExeption
import pytest


class TestLoginPage(BaseCase):

    authorize = False
    
    def test_login_valid(self, credentials):
        self.login_page.login(credentials["user"], credentials["password"])

    def test_login_invalid(self):
        with pytest.raises(PageNotOpenedExeption):
            self.login_page.login("user@mail.ru", "password")
        self.login_page.find(self.login_page.locators.ERROR_MESSAGE)
