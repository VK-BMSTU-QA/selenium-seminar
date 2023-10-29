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

class LoginLocators(BasePageLocators):
    LOGIN_BUTTON_LOCATOR = (
        By.XPATH,
        '//*[@id="popup-login-form-submit"]'
        )
    LOGIN_LOCATOR = (By.NAME, 'login')
    PASSWORD_LOCATOR = (By.NAME, 'password')

class TestLocators(BasePageLocators):
    ENTER_LOCATOR = (
        By.XPATH,
        '//a[contains(@class, button-login)]'
    )
    BLOGS_LOCATOR = (
        By.XPATH,
        '//a[@href="/blog/"]'
        )
    PEOPLE_LOCATOR = (
        By.XPATH,
        '//a[@href="/people/"]'
        )
    PROGRAMS_LOCATOR = (
        By.XPATH,
        '//a[@href="/curriculum/program/"]'
        )
    GRADUATIONS_LOCATOR = (
        By.XPATH,
        '//a[@href="/alumni/"]'
        )
    SHEDULE_LOCATOR = (
        By.XPATH,
        '//a[@href="/schedule/"]'
        )
    JOBS_LOCATOR = (
        By.XPATH,
        '//a[@href="/career/"]'
        )
    PROFILE_LOCATOR = (
        By.XPATH,
        '//*[@id="dropdown-user"]'
        )
    
class ProfileLocators(BasePageLocators):
    CLOTHES_LOCATOR = (
        By.XPATH,
        '//*[@id="profile_clothing_size"]'
    )
    SAVE_LOCATOR = (
       By.NAME, 
       'submit_profile_edit'
       )
    ABOUT_LOCATOR = (
        By.XPATH,
        '//*[@id="profile_about"]'
    )

class EventsPageLocators(BasePageLocators):
    pass
