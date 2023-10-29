import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.profile_page import ProfilePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage
from ui.locators import basic_locators
from selenium.webdriver.support.ui import Select
from additionals import get_login_and_password_from_file
from urllib.parse import urlparse
import time

file_path = 'files/credentials.json'
domain_of_site = 'park.vk.company'
urls = {
    'blogs': 'https://park.vk.company/blog/',
    'people': 'https://park.vk.company/people/',
    'program': 'https://park.vk.company/curriculum/program/mine/',
    'graduations': 'https://park.vk.company/alumni/',
    'shedule': 'https://park.vk.company/schedule/',
    'jobs': 'https://park.vk.company/career/',
}

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, credentials, cookies, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            self.cookies = cookies
            if not check_domain(self.driver):
                self.driver.get('https://park.vk.company')
            add_cookies(self.cookies, self.driver)
        else:
            self.driver.delete_all_cookies()



@pytest.fixture(scope='session')
def credentials():
    return get_login_and_password_from_file(file_path)
    
@pytest.fixture(scope='session')
def cookies(credentials, driver):
        login = credentials.get("login")
        password = credentials.get("password")
        LoginPage(driver).login(login, password)

        return driver.get_cookies()

def check_domain(driver):
    current = driver.current_url
    parsed = urlparse(current)
    return parsed.netloc == domain_of_site

def add_cookies(cookies, driver):
    for cookie in cookies:
        driver.add_cookie(cookie)


class TestLogin(BaseCase):
    authorize = False

    def test_bad_login(self):
        lg = 'log'
        ps = 'pass'
            
        login_page = LoginPage(self.driver)
        login_page.login(lg, ps)
        page = MainPage(self.driver)

        # Profile exist on page
        assert page.find(basic_locators.TestLocators.ENTER_LOCATOR) != None

    def test_good_login(self, credentials):
        login = credentials.get('login')
        password = credentials.get('password')
            
        login_page = LoginPage(self.driver)
        login_page.login(login, password)
        page = MainPage(self.driver)

        # Profile exist on page
        assert page.find(basic_locators.TestLocators.PROFILE_LOCATOR) != None

class TestLK(BaseCase):
    @pytest.mark.parametrize(
        "default_URL, what_click, expected_url",
        [
            (
                urls['blogs'], 
                basic_locators.TestLocators.PEOPLE_LOCATOR, 
                urls['people']
            ),
            (
                urls['program'],
                basic_locators.TestLocators.GRADUATIONS_LOCATOR, 
                urls['graduations']
            ),
        ],
    )
    def test_go_to(self, default_URL, what_click, expected_url):
        page = MainPage(self.driver)
        elem = page.click(what_click, 10)

        assert self.driver.current_url == expected_url

    # Change info about yourself
    def test_change_info(self):
        option_to_take = 'L'

        page = ProfilePage(self.driver)
        prev_size = page.get_current_size()
        page.clear_size()

        # Default value is set
        assert page.get_current_size() == ""
        page.change_size(option_to_take)

        assert page.get_current_size() == option_to_take
        
        page.change_size(prev_size)
        assert page.get_current_size() == prev_size
    
    def test_change_about(self):
        about_text = 'Студент группы ИУ3-73Б?'
        page = ProfilePage(self.driver)
        page.change_about("")

        # Default value is set
        assert page.get_about_info() == ""

        page.change_about(about_text)
        assert page.get_about_info() == about_text

