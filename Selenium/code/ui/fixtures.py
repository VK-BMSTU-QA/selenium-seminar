import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.profile_settings_page import ProfileSettingsPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    if selenoid:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        options.default_capabilities = capabilities

        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',
                                  options=options)
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def profile_settings_page(driver):
    driver.get(ProfileSettingsPage.url)
    return ProfileSettingsPage(driver=driver)


@pytest.fixture(scope='session')
def credentials():
    with open('./files/userdata') as infile:
        return json.load(infile)


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(LoginPage.url)

    login_page = LoginPage(driver)
    login_page.login(**credentials)
    cooks = driver.get_cookies()
    driver.quit()
    return cooks


@pytest.fixture
def restore_settings_about(profile_settings_page: ProfileSettingsPage):
    old_about = profile_settings_page.get_about()
    yield
    profile_settings_page.change_about(old_about)
