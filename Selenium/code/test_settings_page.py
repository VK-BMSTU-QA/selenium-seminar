from base import BaseCase, cookies, credentials
from ui.fixtures import settings_page
import pytest

class TestSettingsPage(BaseCase):
    def test_about(self, settings_page):
        new_about = 'Описание для тестов'
        old_about = settings_page.get_about()
        settings_page.set_about(new_about)
        assert settings_page.get_about() == new_about
        # восстановление описания
        settings_page.set_about(old_about)
        assert settings_page.get_about() == old_about
