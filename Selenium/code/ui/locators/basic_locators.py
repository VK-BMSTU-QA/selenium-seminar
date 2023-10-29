from selenium.webdriver.common.by import By


class LoginPageLocators:
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'nav__button__menu')]")
    EMAIL_LOCATOR = (By.NAME, "login")
    PASSWORD_LOCATOR = (By.NAME, "password")
    ENTER_LOGIN_LOCATOR = (By.NAME, "submit_login")


class BasePageLocators:
    PEOPLE_LOCATOR = (By.XPATH, "//li[contains(@class, 'technopark__menu__item_4')]")
    PROGRAM_LOCATOR = (By.XPATH, "//li[contains(@class, 'technopark__menu__item_41')]")

    USER_OPTIONS_LOCATOR = (By.ID, "dropdown-user-trigger")
    USER_SETTINGS_LOCATOR = (By.XPATH, "//li[contains(@class, 'item-settings')]")


class FeedPageLocators(BasePageLocators):
    pass


class SettingsLocators(BasePageLocators):
    BIO_LOCATOR = (By.NAME, "about")
    SETTING_SUBMIT_LOCATOR = (By.NAME, "submit_profile_edit")
