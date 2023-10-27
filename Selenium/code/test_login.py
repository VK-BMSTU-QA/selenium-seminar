from base import BaseCase, cookies, credentials


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(*credentials)
