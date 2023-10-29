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
    user = os.environ.get("USER_EMAIL")
    password = os.environ.get("USER_PASSWORD")
    if not user or not password:
        raise EnvironmentError("ERR Установи переменные окружения USER_EMAIL и USER_PASSWORD в корневой папке проекта в файле .env")
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
        print("ERR Файл cookies.txt не найден")
        return None
    except json.JSONDecodeError as e:
        print(f"WRN JSONDecodeError (скорее всего файл был пуст): {e}")  # Отладочная информация
        return None


class LoginPage(BasePage):
    url = "https://park.vk.company/"

    def login(self, user, password):
        self.driver.get(self.url)

        # Жмем на кнопку Войти
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/a"))
        )
        login_button.click()

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

    def test_lk1(self):
        # Переходим на страницу "Блоги"
        self.driver.get(self.blog_url)

        # Проверяем, что находимся на правильной странице по заголовку "Все блоги"
        blog_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header"))
        )
        assert blog_header.text == "Все блоги"

        # Находим и кликаем на элемент "Люди" для перехода на страницу "Люди"
        people_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/ul[2]/li[2]/a"))
        )
        people_button.click()

        # Проверяем, что находимся на странице "Люди" по заголовку "Сообщество проекта"
        community_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header"))
        )
        assert community_header.text == "Сообщество проекта"

    def test_lk2(self):
        # Переходим на страницу "Программа"
        self.driver.get(self.program_url)

        # Проверяем, что находимся на правильной странице по надписи "Мои учебные программы"
        my_programs_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "curriculum-nav__item__link"))
        )
        assert my_programs_link.text == "Мои учебные программы"

        # Находим и кликаем на элемент "Выпуски" для перехода на страницу "Выпуски"
        alumni_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/ul[2]/li[4]/a"))
        )
        alumni_button.click()

        # Проверяем, что находимся на странице "Выпуски" по заголовку "Наши выпускники"
        alumni_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-header"))
        )
        assert alumni_header.text == "Наши выпускники"

    def test_lk3(self):
        # Переходим на страницу настроек
        self.driver.get(self.settings_url)

        # Убеждаемся, что активна вкладка "Основное"
        active_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/a[1]"))
        )
        assert "active" in active_tab.get_attribute("class")

        # Убеждаемся, что присутствует вкладка "Уведомления и приватность"
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/a[3]"))
        )

        # Находим textarea для "О себе" и сохраняем текущий текст
        about_textarea = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "profile_about"))
        )
        original_text = about_textarea.text

        # Изменяем текст в textarea
        new_text = original_text + "<3"
        about_textarea.clear()
        about_textarea.send_keys(new_text)

        # Нажимаем кнопку "Сохранить"
        save_button = self.driver.find_element(By.NAME, "submit_profile_edit")
        save_button.click()

        # Проверяем, что появилось сообщение об успешном редактировании
        success_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "profile_settings_success-msg"))
        )
        assert "Вы успешно отредактировали поле: О себе" == success_message.text

        # Возвращаем оригинальный текст в textarea
        about_textarea_after = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "profile_about"))
        )
        about_textarea_after.clear()
        about_textarea_after.send_keys(original_text)

        save_button_after = self.driver.find_element(By.NAME, "submit_profile_edit")
        save_button_after.click()

        success_message_after = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "profile_settings_success-msg"))
        )
        assert "Вы успешно отредактировали поле: О себе" == success_message_after.text
