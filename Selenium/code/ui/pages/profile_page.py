import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class ProfilePage(BasePage):

    locators = basic_locators.ProfilePageLocators()
