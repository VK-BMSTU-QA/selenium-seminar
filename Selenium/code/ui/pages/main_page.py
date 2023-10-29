from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = basic_locators.MainPageLocators()
    name_of_page = "Main"

    @allure.step("Step 2")
    def go_to_events_page(self):
        events_button = self.find(self.locators.EVENTS)

        self.click((By.ID, 'events'))
        return EventsPage(self.driver)
