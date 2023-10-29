import pytest
from base import BaseCase, cookies, credentials, invalid_credentials
from ui.pages.login_page import PageNotOpenedException


class TestLogin(BaseCase):
    authorize = False

    def test_login_valid(self, credentials):
        self.login_page.login(*credentials)
        assert self.driver.current_url == 'https://park.vk.company/feed/'

    def test_login_invalid(self, invalid_credentials):
        with pytest.raises(PageNotOpenedException):
            self.login_page.login(*invalid_credentials)

        self.login_page.check_for_errors()
