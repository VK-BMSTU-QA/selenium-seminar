import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
import ui.locators.basic_locators
from ui.fixtures import get_driver


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        # self.logger = logger

        self.login_page = LoginPage(driver)

        if self.authorize:
            for cookie in request.getfixturevalue('cookies'):
                self.driver.add_cookie(cookie)

            self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
    with open("files/credentials") as creds:
        return creds.readline().split()
        

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(config['url'])

    LoginPage(driver).login(*credentials)
    cookies = driver.get_cookies()

    driver.quit()
    return cookies


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    authorize = False

    locators = ui.locators.basic_locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.locators.LOGIN)

        self.fill_in(self.locators.USER, user)
        self.fill_in(self.locators.PASSWORD, password)

        self.click(self.locators.SUBMIT_LOGIN)

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    pass
    # authorize = False

    # def test_login(self, credentials):
    #     self.login_page.login(*credentials)


class TestLK(BaseCase):

    def test_lk1(self):
        pass

    def test_lk2(self):
        pass

    def test_lk3(self):
        pass
