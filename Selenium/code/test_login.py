import pytest
from base import BaseCase

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)

        assert main_page.url == main_page.driver.current_url
        
    @pytest.mark.parametrize("invalid_creds", [{"email": "stegozavr", "password": "a"}])
    def test_login_neg(self, invalid_creds):
        main_page = self.login_page.login(invalid_creds)

        assert main_page.url != main_page.driver.driver.current_url
    