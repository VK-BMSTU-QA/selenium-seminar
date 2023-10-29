from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators(BasePageLocators):
    OPEN_LOGIN_FORM = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.XPATH, "//input[@name='login' and @type='text']")
    PASSWORD = (By.XPATH, "//input[@name='password' and @type='password']")
    SUBMIT_FORM = (By.NAME, "submit_login")
    ERROR_MESSAGE = (By.CLASS_NAME, "validate-error-login")


class ProfileSettingsPageLocators(BasePageLocators):
    ABOUT = (By.ID, "profile_about")
    SUBMIT_FORM = (By.NAME, "submit_profile_edit")
