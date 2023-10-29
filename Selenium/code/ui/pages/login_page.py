import json
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    login_url = "https://park.vk.company/pages/index/?next=/feed/#auth"

    def login(self, user, password):
        self.driver.get(self.login_url)

        # Вводим логин и пароль
        login_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
        password_input = self.driver.find_element(By.NAME, "password")
        login_input.clear()
        login_input.send_keys(user)
        password_input.clear()
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
