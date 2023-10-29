import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.base_page import ProfilePage


class MainPage(BasePage):

    locators = basic_locators.MainPageLocators()
    url = 'https://park.vk.company/blog/'

    @allure.step("Go to tab")
    def go_to_tab(self, tab_name, timeout=5):
        if tab_name == "BLOGS":
            self.go_to_blogs_tab(timeout)
        elif tab_name == "PEOPLE":
            self.go_to_people_tab(timeout)
        elif tab_name == "PEOPLE_RELEASES":
            self.go_to_releases_tab(timeout)
        elif tab_name == "PROGRAMS":
            self.go_to_program_tab(timeout)
        elif tab_name == "PROFILE":
            self.go_to_profile(timeout)

    @allure.step("Go to people tab")
    def go_to_people_tab(self, timeout=5):
        self.click(self.locators.PEOPLE, timeout)

    @allure.step("Go to releases tab")
    def go_to_releases_tab(self, timeout=5):
        self.click(self.locators.PEOPLE_RELEASES, timeout)

    @allure.step("Go to blogs tab")
    def go_to_blogs_tab(self, timeout=5):
        self.click(self.locators.BLOGS, timeout)

    @allure.step("Go to program tab")
    def go_to_program_tab(self, timeout=5):
        self.click(self.locators.PROGRAM, timeout)

    @allure.step("Go to profile")
    def go_to_profile(self, timeout=5):
        self.click(self.locators.PROFILE, timeout)
        return ProfilePage(self.driver)
