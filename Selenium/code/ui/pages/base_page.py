import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://park.vk.company/feed/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        return self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem
    
    @allure.step('Fill')
    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem.send_keys(text)
        return elem
