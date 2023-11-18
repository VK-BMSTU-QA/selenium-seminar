from base import BaseCase
from ui.pages.profile_settings_page import ProfileSettingsPage


class TestProfileSettingsLogin(BaseCase):

    def test_change_about(self, profile_settings_page: ProfileSettingsPage,
                          restore_settings_about):
        new_about = 'New about'
        profile_settings_page.change_about(new_about)
        assert profile_settings_page.get_about() == new_about
