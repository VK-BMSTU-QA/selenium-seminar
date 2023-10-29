import time
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict

import allure
import pytest
import json
from _pytest.fixtures import FixtureRequest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.base_page import BasePage
from ui.fixtures import driver, get_driver


@pytest.fixture(scope='session')
def credentials() -> Dict[str, str]:
    with open('../credentials.json') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver('chrome')
    login_page = LoginPage(driver)
    login_page.login(credentials["user"], credentials["password"])
    return driver.get_cookies()


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

    @pytest.fixture(scope='function')
    def authorize(self, driver, config, cookies, request: FixtureRequest):
        if self.authorize:
            for cookie in cookies:
                driver.add_cookie(cookie)


class LoginPageLocators:
    LOGIN = (By.ID, "popup-login-form-submit")
    USER_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')


class LoginPage(BasePage):
    url = 'https://park.vk.company/pages/index/?next=/blog/view/4/#auth'

    def setTextInLocatorElement(self, locator, text):
        element: WebElement = self.find(locator)

        element.clear()
        element.send_keys(text)

    def login(self, user, password):
        submit: WebElement = self.find(LoginPageLocators.LOGIN)
        self.setTextInLocatorElement(LoginPageLocators.USER_FIELD, user)
        self.setTextInLocatorElement(LoginPageLocators.PASSWORD_FIELD, password)

        submit.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Блоги")))

        return MainPage(self.driver)


def main_page_widget_locator(text):
    return By.LINK_TEXT, text


class MainPageLocators:
    USER_DROPDOWN = (By.ID, "dropdown-user-trigger")
    PERSONAL_CABINET = (By.CLASS_NAME, 'item-personal-cabinet')
    SEARCH_START = (By.CLASS_NAME, 'js-show-search')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def change_widget(self, from_name, to_name):
        from_element: WebElement = self.find(main_page_widget_locator(from_name))
        from_element.click()

        to_element: WebElement = self.find(main_page_widget_locator(to_name))
        to_element.click()

    def navigate_to_personal_cabinet(self):
        dropdown_element: WebElement = self.find(MainPageLocators.USER_DROPDOWN)
        dropdown_element.click()
        cabinet_link: WebElement = self.find(MainPageLocators.PERSONAL_CABINET)
        cabinet_link.click()

    @allure.step('Search')
    def search_and_assert_with_awaiting_content(self, query, awaiting):
        search_start: WebElement = self.find(MainPageLocators.SEARCH_START)
        search_start.click()

        search_input: WebElement = self.driver.switch_to.active_element

        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).send_keys(query).send_keys(Keys.ENTER).perform()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "people-list")))

        self.my_assert(awaiting)

    @allure.step("Step 1")
    def my_assert(self, awaiting_text):
        assert awaiting_text in self.driver.page_source
        self.driver.quit()


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, setup, credentials, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        assert "Блоги" in self.driver.page_source
        self.driver.quit()


class TestLK(BaseCase):

    def test_lk1(self, setup, credentials, cookies, authorize):
        main_page = MainPage(self.driver)
        main_page.change_widget('Блоги', 'Расписание')
        assert "Дисциплина" in self.driver.page_source
        self.driver.quit()

    def test_lk2(self, setup, credentials, cookies, authorize):
        main_page = MainPage(self.driver)
        main_page.navigate_to_personal_cabinet()
        assert "Активность на" in self.driver.page_source
        self.driver.quit()

    def test_lk3(self, setup, credentials, cookies, authorize):
        main_page = MainPage(self.driver)
        main_page.search_and_assert_with_awaiting_content("Чернега", "Елена Владимировна")
