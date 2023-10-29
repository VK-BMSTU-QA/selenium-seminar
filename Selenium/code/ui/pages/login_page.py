import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
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
    