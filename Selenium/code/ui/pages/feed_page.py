from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
# from ui.pages.events_page import EventsPage


class FeedPage(BasePage):
    url = 'https://park.vk.company/feed/'

    locators = basic_locators.FeedPageLocators
