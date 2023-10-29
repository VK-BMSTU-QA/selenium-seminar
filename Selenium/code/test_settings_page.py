from base import BaseCase, cookies, credentials
from ui.fixtures import settings_page
import pytest


class TestSettingsPage(BaseCase):
    @pytest.mark.parametrize('contents', ['Тестируем...'])
    def test_about(self, settings_page, contents):
        settings_page.edit_about(contents)
        assert settings_page.about_contents() == contents

    @pytest.mark.parametrize('size', ['L'])
    def test_clothes_size(self, settings_page, size):
        settings_page.set_clothes_size(size)
        assert settings_page.clothes_size() == size
