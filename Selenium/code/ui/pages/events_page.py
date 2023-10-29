from ui.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class EventsPage(BasePage):
    url: str

    def __init__(self, driver: RemoteWebDriver, url: str):
        self.url = f'https://park.vk.company/{url}'
        super().__init__(driver)
