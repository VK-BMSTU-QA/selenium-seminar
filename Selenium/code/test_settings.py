import pytest
from base import BaseCase

class TestSettings(BaseCase):
    authorize = True

    @pytest.mark.parametrize('about', ['Студент ИУ5-53Б'])
    def test_about(self, about, settings_page, cookies):

        self.settings_page.change_about(about)

        changed_about = self.settings_page.get_about()
        assert changed_about == about

    @pytest.mark.parametrize('gender', ['f', 'm'])
    def test_gendert(self, gender, settings_page, cookies):
        self.settings_page.change_gender(gender)

        changed_gender = self.settings.get_gender()

        assert changed_gender == gender
        