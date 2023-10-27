import pytest
from base import BaseCase, cookies, credentials

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(*credentials)


class TestLK(BaseCase):

    def test_lk1(self):
        pass

    def test_lk2(self):
        pass

    def test_lk3(self):
        pass
