from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]')
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass


class LoginPageLocators(BasePageLocators):
    OPEN_LOGIN_FORM = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.XPATH, "//input[@name='login' and @type='text']")
    PASSWORD = (By.XPATH, "//input[@name='password' and @type='password']")
    SUBMIT_FORM = (By.XPATH, "//*[@id='popup-login-form-submit']/span")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='popup-login-form']/p[2]")


class ProfileSettingsPageLocators(BasePageLocators):
    ABOUT = (By.ID, "profile_about")
    SUBMIT_FORM = (By.NAME, "submit_profile_edit")
