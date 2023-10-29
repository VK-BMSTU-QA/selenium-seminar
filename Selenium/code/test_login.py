import pytest
from _pytest.fixtures import FixtureRequest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from dotenv import load_dotenv

from ui.pages.base_page import BasePage


load_dotenv()


class BaseCase:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, credentials, cookies, request: FixtureRequest):
        self.driver = driver
        self.config = config

        login_page = LoginPage(driver)
        if not cookies:
            self.main_page = login_page.login(credentials["user"], credentials["password"])
        else:
            self.driver.get(MainPage.url)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()


@pytest.fixture(scope="session")
def credentials():
    user = os.environ.get("login_or_email")
    password = os.environ.get("password")
    if not user or not password:
        raise EnvironmentError("Ошибка: переменные окружения для авторизации не установлены: в файле .env задай "
                               "переменные login_or_email и password")
    return {
        "user": user,
        "password": password
    }


@pytest.fixture(scope="session")
def cookies():
    try:
        if not os.path.exists("cookies.txt"):
            with open("cookies.txt", "w") as f:
                json.dump({}, f)

        with open("cookies.txt", "r") as f:
            cookies_data = f.read()
            return json.loads(cookies_data)
    except FileNotFoundError:
        print("Ошибка: Файл cookies.txt не найден")
        return None
    except json.JSONDecodeError as e:
        print(f"WRN JSONDecodeError (скорее всего файл был пуст): {e}")  # Отладочная информация
        return None


class LoginPage(BasePage):
    login_url = "https://park.vk.company/pages/index/?next=/feed/#auth"

    def login(self, user, password):
        self.driver.get(self.login_url)

        # Вводим логин и пароль
        login_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
        password_input = self.driver.find_element(By.NAME, "password")
        login_input.send_keys(user)
        password_input.send_keys(password)

        # Жмем на кнопку Войти
        submit_button = self.driver.find_element(By.ID, "popup-login-form-submit")
        submit_button.click()

        # Ждем загрузки страницы после входа
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "username")))

        # Загружаем куки в файл кук
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
            json.dump(cookies, f)

        return MainPage(self.driver)


class MainPage(BasePage):
    url = "https://park.vk.company/feed/"


class TestLogin(BaseCase):
    def test_login(self, credentials):
        assert MainPage.url in self.driver.current_url

        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "dropdown-user-trigger"))
        )
        clickable_element.click()

        expected_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "logout"))
        )

        assert expected_element is not None


class TestLK(BaseCase):
    blog_url = "https://park.vk.company/blog/"
    program_url = "https://park.vk.company/curriculum/program/mine/"
    settings_url = "https://park.vk.company/cabinet/settings/"

    submit_profile_edit = "submit_profile_edit"
    profile_settings_success_msg = "profile_settings_success-msg"
    profile_edit_success_message = "Вы успешно отредактировали поле: О себе"
    profile_about_id = "profile_about"

    def __change_about_info__(self, about_textarea, new_text):
        about_textarea.clear()
        about_textarea.send_keys(new_text)

        # Нажимаем кнопку "Сохранить"
        save_button = self.driver.find_element(By.NAME, self.submit_profile_edit)
        save_button.click()

        success_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.profile_settings_success_msg))
        )

        # Проверяем, что появилось сообщение об успешном редактировании
        assert self.profile_edit_success_message == success_message.text

    @pytest.mark.parametrize(
        "url,header_selector,expected_header,header_xpath,expected_moved_selector,expected_moved_header", [
            ("https://park.vk.company/blog/", "page-header", "Все блоги", '//a[@href="' + "/people/" + '"]',
             "page-header", "Сообщество проекта"),
            ("https://park.vk.company/curriculum/program/mine/", "curriculum-nav__item__link", "Мои учебные программы",
             '//a[@href="' + "/alumni/" + '"]', "page-header", "Наши выпускники")
        ])
    def test_lk_generic(self, url, header_selector, expected_header, header_xpath, expected_moved_selector,
                        expected_moved_header):
        self.driver.get(url)

        start_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, header_selector))
        )
        assert start_header.text == expected_header

        header_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, header_xpath))
        )
        header_button.click()

        # Проверяем, что находимся на странице "Люди" по заголовку "Сообщество проекта"
        expected_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, expected_moved_selector))
        )
        assert expected_header.text == expected_moved_header

    def test_change_about_info(self):
        # Переходим на страницу настроек
        self.driver.get(self.settings_url)

        active_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/cabinet/settings/']"))
        )

        assert "active" in active_tab.get_attribute("class")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/cabinet/settings/site/']"))
        )

        # Находим textarea для "О себе" и сохраняем текущий текст
        about_textarea = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, self.profile_about_id))
        )
        original_text = about_textarea.text

        appended_text = "---этот текст добавлен в рамках теста"

        # Изменяем текст в textarea
        new_text = original_text + appended_text

        self.__change_about_info__(about_textarea, new_text)

        # Возвращаем оригинальный текст в textarea
        about_textarea_after = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, self.profile_about_id))
        )

        assert about_textarea_after.text == original_text + appended_text

        self.__change_about_info__(about_textarea_after, original_text)

