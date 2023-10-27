from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class MainPageLocators(BasePageLocators):
    pass


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.LINK_TEXT, 'Войти')
    USER = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_LOGIN = (By.NAME, 'submit_login')
