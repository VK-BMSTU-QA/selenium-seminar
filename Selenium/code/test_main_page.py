from base import BaseCase, cookies, credentials
from ui.locators.basic_locators import BasePageLocators
from ui.fixtures import main_page
import pytest


class TestMainPage(BaseCase):
    def go_to_menu_section(self, main_page, menu_section_name, menu_section_url):
        main_page.set_menu_section(menu_section_name)
        main_page.check_url(f'https://park.vk.company/{menu_section_url}')

        new_section = main_page.get_menu_section(menu_section_name)
        new_section_class = new_section.find_element(
            *BasePageLocators.PARENT).get_dom_attribute('class')
        assert 'active' in new_section_class

    @pytest.mark.parametrize('section_1,section_2', [
        (('Люди', 'people/'), ('Блоги', 'blog/')),
        (('Программа', 'curriculum/program/mine/'), ('Выпуски', 'alumni/')),
    ])
    def test_moving_sections_header(self, main_page, section_1, section_2):
        self.go_to_menu_section(main_page, *section_1)
        self.go_to_menu_section(main_page, *section_2)

    @pytest.mark.parametrize('student_name', [
        "Мяделец", "Роменский", "Габриелян" 
    ])
    def test_like_to_student(self, main_page, student_name):
        main_page.search(student_name)
        assert not main_page.check_text_on_page("Поиск не дал результатов")  
        main_page.click(main_page.locators.FIRST_SEARCH_ITEM)
        main_page.click(main_page.locators.LIKE_USER)
        main_page.find(main_page.locators.HAS_LIKE)






