from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')


class MainPageLocators(BasePageLocators):
    PEOPLE = (By.LINK_TEXT, 'Люди')
    BLOGS = (By.LINK_TEXT, 'Блоги')
    PROGRAM = (By.LINK_TEXT, 'Программа')
    ALUMNI = (By.LINK_TEXT, 'Выпуски')


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.LINK_TEXT, 'Войти')
    USER = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_LOGIN = (By.NAME, 'submit_login')
