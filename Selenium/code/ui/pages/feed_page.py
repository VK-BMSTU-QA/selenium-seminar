from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class FeedPage(BasePage):
    url = 'https://park.vk.company/feed/'

    locators = basic_locators.FeedPageLocators
