from selenium.webdriver.common.by import By
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains, Keys


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = basic_locators.MainPageLocators()

    def get_menu_section(self, menu_section_name):
        return self.find((By.LINK_TEXT, menu_section_name))

    def set_menu_section(self, menu_section_name):
        self.click((By.LINK_TEXT, menu_section_name))

    def search(self, query):
        search: WebElement = self.find(self.locators.SEARCH)
        search.click()

        search_input: WebElement = self.driver.switch_to.active_element

        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).send_keys(query).send_keys(Keys.ENTER).perform()

    # @allure.step("Step 1")
    # def my_assert(self, awaiting_text):
    #     assert awaiting_text in self.driver.page_source

