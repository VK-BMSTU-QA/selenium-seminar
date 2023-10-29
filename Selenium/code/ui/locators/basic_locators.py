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
    LOGIN_BTN = (By.LINK_TEXT, 'Войти')
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWD_FIELD = (By.NAME, 'password')
    SUBMIT_LOGIN_BTN = (By.NAME, 'submit_login')
    ERR_MSG = (By.CLASS_NAME, 'error-message')


class SettingsPageLocators(BasePageLocators):
    ABOUT_INPUT = (By.ID, 'profile_about')
    SAVE_BTN = (By.NAME, 'submit_profile_edit')
