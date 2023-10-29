import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.profile_page import ProfilePage
from base import BaseCase
from ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By

testdata_single = [
    ('//*[@id="header"]/ul[2]/li[1]', 'Все блоги'),
    ('//*[@id="header"]/ul[2]/li[2]', 'Сообщество проекта'),
    ('//*[@id="header"]/ul[2]/li[3]', 'Основные программы')
]

testdata_chain = [
    ('//*[@id="header"]/ul[2]/li[1]', '//*[@id="header"]/ul[2]/li[2]', 'Сообщество проекта'),
    ('//*[@id="header"]/ul[2]/li[2]', '//*[@id="header"]/ul[2]/li[3]', 'Основные программы'),
    ('//*[@id="header"]/ul[2]/li[3]', '//*[@id="header"]/ul[2]/li[1]', 'Все блоги')
]

class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def open_part(self, xpath):
        self.click((By.XPATH, xpath))


class TestMainPage(BaseCase):


    @pytest.mark.parametrize("path,expected", testdata_single)
    def test_click_tabs(self, path, expected):
        page = MainPage(self.driver)
        page.open_part(path)
        assert expected in self.driver.page_source

    @pytest.mark.parametrize("first, second, expected", testdata_chain)
    def test_chain_click_tabs(self, first, second, expected):
        page = MainPage(self.driver)
        page.open_part(first)
        page.open_part(second)
        assert expected in self.driver.page_source

    @pytest.mark.skip
    def change_info(self):
        profile_page = ProfilePage(self.driver)
        element = profile_page.find((By.XPATH, '//*[@id="profile_about"]'))
        element.send_keys('test record')
        profile_page.click((By.XPATH, '//*[@id="content"]/div[2]/div[1]/form/div[2]/button'))
        
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
