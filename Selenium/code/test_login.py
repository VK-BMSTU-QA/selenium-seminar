import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        return {
             'login': 'password',
             'password': 'login'
        }


@pytest.fixture(scope='session')
def cookies(credentials, config):
    return 


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(By.XPATH, '//*[@id="header"]/div/div[2]')
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.click()




# class TestLK(BaseCase):

#     def test_lk1(self):
#         pass

#     def test_lk2(self):
#         pass

#     def test_lk3(self):
#         pass
