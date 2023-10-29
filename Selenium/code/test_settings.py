import pytest

from base import BaseCase, cookies, credentials
from ui.fixtures import settings_page


class TestSettings(BaseCase):
    authorize = True
    url = 'https://park.vk.company/cabinet/settings/'

    values = [
        'Студент ИУ6, автотестер :)',
        'Студент ИУ6'
    ]

    @pytest.mark.parametrize('new_value', values)
    def test_about_field(self, settings_page, new_value):
        settings_page.fill_about_input(new_value)
        settings_page.submit()

        assert settings_page.get_about_value() == new_value

