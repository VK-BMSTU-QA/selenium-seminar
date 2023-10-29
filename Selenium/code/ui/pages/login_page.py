from Selenium.code.ui.pages.base_page import BasePage
from Selenium.code.ui.locators.park_vk_locators import LoginLocators
from Selenium.code.ui.pages.main_page import MainPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    authorize = False

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

    def check_for_errors(self):
        self.find(self.locators.ERROR_MESSAGE)
