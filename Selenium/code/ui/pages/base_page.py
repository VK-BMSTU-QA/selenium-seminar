import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from ui.locators import basic_locators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    url = 'https://park.vk.company'

    locators = basic_locators.BasePageLocators()
    locators_main = basic_locators.MainPageLocators()

    @allure.step('Is opened')
    def is_opened(self, timeout=5):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(
            f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}'
        )

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.is_opened()

    @allure.step('Wait')
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Find')
    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
