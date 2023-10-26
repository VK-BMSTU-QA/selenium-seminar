import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.fixtures import get_driver
from ui.locators.park_vk_locators import LoginLocators, TabLocators
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        # self.logger = logger

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                driver.add_cookie(cookie)

            self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
    with open('files/credentials.txt', 'r') as file:
        login, password = file.readline().split(':')
        return login, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    url = config['url']

    driver.get(url)

    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()

    driver.quit()

    return cookies


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    locators = LoginLocators()

    def login(self, user, password):
        login_btn = self.driver.find_element(*self.locators.BTN_LOCATOR)
        login_btn.click()

        modal_window = self.driver.find_element(*self.locators.MODAL_WINDOW)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(modal_window))

        login_input = self.driver.find_element(*self.locators.INPUT_LOGIN)
        password_input = self.driver.find_element(*self.locators.INPUT_PASSWORD)

        login_input.send_keys(user)
        password_input.send_keys(password)

        submit_btn = self.driver.find_element(*self.locators.SUBMIT_BTN)
        submit_btn.click()

        wait.until(EC.url_changes('https://park.vk.company/feed/'))

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(*credentials)


class TestTab(BaseCase):
    authorize = True

    tab_locators = TabLocators()

    def test_people_tab(self):
        self.driver.get('https://park.vk.company/blog/')

        people_tab = self.driver.find_element(*self.tab_locators.PEOPLE_TAB)
        people_tab.click()

        assert self.driver.current_url == 'https://park.vk.company/people/'


class TestLK(BaseCase):

    def test_lk1(self):
        print('passed')

    def test_lk2(self):
        pass

    def test_lk3(self):
        pass
