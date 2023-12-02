from base import BaseCase, cookies, credentials
from ui.fixtures import settings_page
import pytest


class TestProfile(BaseCase):
    @pytest.mark.parametrize('contents', ['Тестируем...'])
    def test_about(self, settings_page, contents):
        old_about = settings_page.about_contents()

        settings_page.edit_about(contents)
        assert settings_page.about_contents() == contents

        settings_page.edit_about(old_about)
        assert settings_page.about_contents() == old_about

    @pytest.mark.parametrize('size', ['L'])
    def test_clothes_size(self, settings_page, size):
        old_size = settings_page.clothes_size()

        settings_page.set_clothes_size(size)
        assert settings_page.clothes_size() == size

        settings_page.set_clothes_size(old_size)
        assert settings_page.clothes_size() == old_size
