from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class VKMainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_tab(self, tab_name):
        self.click((By.LINK_TEXT, tab_name))
