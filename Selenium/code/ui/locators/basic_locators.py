from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass

class LoginPageLocators(BasePageLocators):
    LOGIN = (By.LINK_TEXT, 'Войти')
    USER = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_LOGIN = (By.NAME, 'submit_login')
