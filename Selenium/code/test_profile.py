import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.profile_page import ProfilePage
from base import BaseCase
from ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By


@pytest.fixture
def profile_page(driver):
    driver.get('https://park.vk.company/cabinet/settings/')
    return ProfilePage(driver=driver)

class TestProfilePage(BaseCase):
    
    def test_change_info(self):

        profile_page = ProfilePage(self.driver)
        element = profile_page.find((By.XPATH, '//*[@id="profile_about"]'))
        element.send_keys('test record')
        profile_page.click((By.XPATH, '//*[@id="content"]/div[2]/div[1]/form/div[2]/button'))
        
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
