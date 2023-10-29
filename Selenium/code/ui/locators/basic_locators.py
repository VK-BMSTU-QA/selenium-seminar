from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')


class MainPageLocators(BasePageLocators):
    SEARCH = (By.CLASS_NAME, 'js-show-search')
    FIRST_SEARCH_ITEM = (By.XPATH, "//div[@class='people-list']//tr//div[@class='name']//a")
    LIKE_USER = (By.XPATH, "//div[@class='vote-up vote-btn']")
    HAS_LIKE = (By.XPATH, "//div[@class='profile-top']//div[contains(@class, 'voted-up')]")

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
