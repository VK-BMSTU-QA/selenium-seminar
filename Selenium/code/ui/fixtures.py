import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    service = Service(executable_path="/Users/mochalovskiy/Technopark/QA/selenium-seminar/Selenium/chromedriver_mac_arm64/chromedriver-mac-x64/chromedriver")
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        driver = webdriver.Chrome(options=options, service=service)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        options = Options()
        service = Service(executable_path="/Users/mochalovskiy/Technopark/QA/selenium-seminar/Selenium/chromedriver_mac_arm64/chromedriver-mac-x64/chromedriver")
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
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
