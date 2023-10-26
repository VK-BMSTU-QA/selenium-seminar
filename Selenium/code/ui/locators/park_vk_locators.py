from selenium.webdriver.common.by import By


class LoginLocators:
    BTN_LOCATOR = (By.LINK_TEXT, 'Войти')
    MODAL_WINDOW = (By.ID, 'popup-login')
    INPUT_LOGIN = (By.NAME, 'login')
    INPUT_PASSWORD = (By.NAME, 'password')
    SUBMIT_BTN = (By.ID, 'popup-login-form-submit')


class TabLocators:
    BLOG_TAB = (By.LINK_TEXT, 'Блоги')
    PEOPLE_TAB = (By.LINK_TEXT, 'Люди')
    PLAN_TAB = (By.LINK_TEXT, 'Программа')
