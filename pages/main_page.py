import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
class Main_page(Base):


    """Locators"""
    # Локатор поля ПОИСК на Главной странице
    search = "//input[@id='smart-title-search-input']"
    # Локатор иконки логотипа на Главной странице
    logo = "//div[@class='sh-logo']"


    """Getters"""

    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search)))

    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.logo)))



    """Actions"""
    def click_logo(self):
        self.get_logo().click()
        print("Переход на Главную страницу")


    """Methods"""
    def enter_search(self):
        self.get_input_search().click()
        self.get_input_search().send_keys("Сертификат")
        self.get_input_search().send_keys(Keys.ENTER)
        self.scroll_page(0, 150)
        print("Поиск отработал корректно!")

    def return_main_page(self):
        self.click_logo()
        self.assert_url("https://pitergsm.ru/")

