from selenium.webdriver.common.by import By

'''
COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
'''

class BasePageLocators:
    pass

class MainPageLocators(BasePageLocators):
    BLOGS = (By.LINK_TEXT, 'Блоги')
    PROGRAM = (By.LINK_TEXT, 'Люди')
    PEOPLE = (By.LINK_TEXT, 'Программа')
    PEOPLE_RELEASES = (By.LINK_TEXT, 'Выпуски')
    PROFILE = (By.CLASS_NAME, 'full_name')

class LoginPageLocators(BasePageLocators):
    LOGIN_BTN_MAIN_SCREEN = (By.CLASS_NAME, 'button-login')
    EMAIL_INPUT = (By.NAME, 'login')
    PASS_INPUT = (By.NAME, 'password')
    LOGIN_BTN_FORM = (By.NAME, 'submit_login')

class ProfilePageLocators(BasePageLocators):
    SETTINGS = (By.LINK_TEXT, 'Настройки')

class SettingsPageLocators(BasePageLocators):
    GENDER = (By.ID, 'profile_sex')
    ABOUT = (By.ID, 'profile_about')
    SUBMIT = (By.ID, 'submit_profile_edit')
