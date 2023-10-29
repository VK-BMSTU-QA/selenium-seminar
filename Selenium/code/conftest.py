from ui.fixtures import *
from ui.pages.login_page import LoginPage
import json

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://park.vk.company')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }

@pytest.fixture(scope='session')
def cookies(credentials, config):
    print(config['browser'])
    driver = get_driver(config['browser'])
    driver.get(config['url'])

    login_page = LoginPage(driver)
    login_page.login(credentials['login'], credentials['password'])
    session_cookies = driver.get_cookies()
    driver.quit()
    return session_cookies

@pytest.fixture(scope='session')
def credentials():
        
        with open('files/creds.json') as cred_file:
            creds_object = json.load(cred_file)
        return {
             'login': creds_object['login'],
             'password': creds_object['pass']
        }

@pytest.fixture(scope='session')
def false_credentials():
     return {
          'login':'admin',
          'password':'admin'
     }

