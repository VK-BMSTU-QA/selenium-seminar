import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage, PageNotOpenedExeption
from ui.pages.main_page import MainPage
from base import BaseCase, credentials, cookies, false_credentials
from selenium.webdriver.common.by import By
from ui.fixtures import get_driver
import json


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click((By.XPATH, '//*[@id="header"]/div/div[2]'))
        login_input = self.find((By.XPATH, '//*[@id="popup-login-form"]/div[1]/p[1]/input'))
        password_input = self.find((By.XPATH, '//*[@id="popup-login-form"]/div[1]/p[2]/input'))
        login_input.send_keys(user)
        password_input.send_keys(password)
        self.click((By.XPATH, '//*[@id="popup-login-form-submit"]'))
        return MainPage(self.driver)



# class TestLoginFail(BaseCase):
#     authorize = False

#     def test_login_fail(self, credentials):
#         pass

class TestLoginSuccess(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials['login'], credentials['password'])
        
    def test_login_fail(self, false_credentials):
        try:
            login_page = LoginPage(self.driver)
            login_page.login(false_credentials['login'], false_credentials['password'])
        except PageNotOpenedExeption:
            assert 'Учётные данные неверны' in self.driver.page_source    
        


# class TestLK(BaseCase):

#     def test_lk1(self):
#         pass

#     def test_lk2(self):
#         pass

#     def test_lk3(self):
#         pass
