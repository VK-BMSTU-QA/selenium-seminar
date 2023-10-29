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
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage


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

    @pytest.mark.parametrize("url,header_selector,expected_header,header_xpath,expected_moved_selector,expected_moved_header", [
        ("https://park.vk.company/blog/", "page-header", "Все блоги", '//a[@href="'+"/people/"+'"]', "page-header", "Сообщество проекта"),
        ("https://park.vk.company/curriculum/program/mine/", "curriculum-nav__item__link", "Мои учебные программы", '//a[@href="'+"/alumni/"+'"]', "page-header", "Наши выпускники")
    ])
    def test_lk_generic(self, url, header_selector, expected_header, header_xpath, expected_moved_selector, expected_moved_header):
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
