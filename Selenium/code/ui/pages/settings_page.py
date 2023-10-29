import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.base_page import ProfilePage
from selenium.webdriver.support.select import Select


class SettingsPage(BasePage):

    locators = basic_locators.SettingsPageLocators()
    utl = 'https://park.vk.company/cabinet/settings/'

    @allure.step("Change gender")
    def change_gender(self, gender, timeout=5): # gender = m|f
        gender = Select(self.find(self.locators.GENDER))
        gender.select_by_value(gender)
        self.__submit(timeout)

    @allure.step("Change about info")
    def change_about(self, text, timeout=5):
        self.fill(self.locators.ABOUT, text, timeout)
        self.__submit(timeout)

    @allure.step("Get about info")
    def get_about(self, timeout=5):
        return self.find(self.locators.ABOUT, timeout).text
    
    @allure.step("Get gender")
    def get_gender(self, timeout=5):
        gender = Select(self.find(self.locators.GENDER))
        return gender.first_selected_option().get_attribute('value')
        

    def __submit(self, timeout=5):
        self.click(self.locators.SUBMIT, timeout)
