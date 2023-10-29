import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from base import BaseCase
from ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By



class ProfilePage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
