import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.profile_page import ProfilePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage
from ui.locators import basic_locators
from selenium.webdriver.support.ui import Select
from additionals import getLoginAndPasswordFromFile
from urllib.parse import urlparse

filePath = 'files/credentials'
domainOfSite = 'park.vk.company'
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
            print("Need auth")
            self.cookies = cookies
            if not checkDomain(self.driver):
                self.driver.get('https://park.vk.company')
            addCookies(self.cookies, self.driver)



@pytest.fixture(scope='session')
def credentials():
    return getLoginAndPasswordFromFile(filePath)
    
@pytest.fixture(scope='session')
def cookies(credentials, driver):
        login = credentials.get("login")
        password = credentials.get("password")
        LoginPage(driver).login(login, password)

        return driver.get_cookies()

def checkDomain(driver):
    current = driver.current_url
    parsed = urlparse(current)
    return parsed.netloc == domainOfSite

def addCookies(cookies, driver):
    for cookie in cookies:
        driver.add_cookie(cookie)


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)

        login = credentials.get("login")
        password = credentials.get("password")

        login_page.login(login, password)
        page = MainPage(self.driver)

        # Profile exist on page
        assert page.find(basic_locators.TestLocators.PROFILE_LOCATOR) != None

class TestLK(BaseCase):
    @pytest.mark.parametrize(
        "defaultURL, whatClick, expectedUrl",
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
    def test_goTo(self, defaultURL, whatClick, expectedUrl):
        page = MainPage(self.driver)
        elem = page.click(whatClick, 10)

        assert self.driver.current_url == expectedUrl

    # Change info about yourself
    def test_changeInfo(self):
        optionToTake = 'L'

        page = ProfilePage(self.driver)
        page.clearSize()

        # Default value is set
        assert page.getCurrentSize() == ""
        page.changeSize(optionToTake)

        assert page.getCurrentSize() == optionToTake
    
    def test_changeAbout(self):
        aboutText = 'Студент группы ИУ3-73Б?'
        page = ProfilePage(self.driver)
        page.changeAbout("")

        # Default value is set
        assert page.getAboutInfo() == ""

        page.changeAbout(aboutText)
        assert page.getAboutInfo() == aboutText

