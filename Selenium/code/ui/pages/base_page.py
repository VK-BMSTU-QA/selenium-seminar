import logging
import time

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY = 3


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators
    sections_locators = {
        'Люди': locators.PEOPLE_LOCATOR,
        'Программа': locators.PROGRAM_LOCATOR,
    }

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def fill_field(self, locator, string):
        field = self.find(locator)
        field.clear()
        field.send_keys(string)

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=5):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def move_to(self, section_name):
        locator = self.sections_locators.get(section_name, None)

        if locator is not None:
            self.click(locator)

    def move_to_settings(self):
        self.click(self.locators.USER_OPTIONS_LOCATOR)
        self.click(self.locators.USER_SETTINGS_LOCATOR)
