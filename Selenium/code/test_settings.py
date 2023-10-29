import pytest

from test_login import BaseCase


class TestSettings(BaseCase):
    @pytest.mark.parametrize('text', ['Это тест', ''])
    def test_about_me(self, settings_page, text):
        settings_page.edit_about(text)
        assert settings_page.get_about() == text
