import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.feed_page import FeedPage


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver(config, download_dir=temp_dir)
        browser.get(url)

    yield browser
    browser.quit()


def get_driver(config, download_dir=None):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if browser_name == 'chrome':
        options = Options()

        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})

        if selenoid:
            options.add_experimental_option("prefs", {"download.default_directory": '/home/\'Загрузки\'/'})
            capabilities = {
                'browserName': 'chrome',
                'version': '95.0'
            }

            if vnc:
                capabilities['version'] += '_vnc'
                capabilities['enableVNC'] = True

            browser = webdriver.Remote(selenoid, options=options,
                                       desired_capabilities=capabilities)
        else:
            manager = ChromeDriverManager()
            browser = webdriver.Chrome(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='session')
def credentials():
    with open('files/userdata', 'r') as f:
        lines = f.readlines()

    email = lines[0].strip()
    password = lines[1].strip()

    return email, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

