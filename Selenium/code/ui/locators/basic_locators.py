from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')


class MainPageLocators(BasePageLocators):
    ACTIVE_TAB = (
        By.XPATH,  '//*[contains(@class, "nav")]//*[contains(@class, "active")]')


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.LINK_TEXT, 'Войти')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message')
    USER = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_LOGIN = (By.NAME, 'submit_login')


class SettingsPageLocators(BasePageLocators):
    ABOUT = (By.ID, 'profile_about')
    CLOTHES_SIZE = (By.ID, 'profile_clothing_size')
    SUBMIT_PROFILE_EDIT = (By.NAME, 'submit_profile_edit')
