from datetime import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium import webdriver


class Login_page(Base):

    url = "https://pitergsm.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login = "//a[@data-pop='pop-login']"
    email = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    enter = "//input[@name='Login']"
    success_word = "//a[contains(@class, 'sh-nav__link') and contains(text(), 'Личный кабинет')]"


    # Getters
    def get_login_account(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.login)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.enter)))

    def get_success_word(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.success_word)))



    # Actions
    def click_login_account(self):
        self.get_login_account().click()
        print("Click Account")

    def input_email(self):
        self.get_email().send_keys("lexaeliseev")
        print("Input Email")

    def input_password(self):
        self.get_password().send_keys("PiterPiter")
        print("Input Password")

    def click_enter(self):
        self.get_enter().click()
        print("Click Enter")


    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_account()
        self.input_email()
        self.input_password()
        self.click_enter()
        self.assert_word(self.get_success_word(), "Личный кабинет")
        print("Авторизация в систему прошла успешно!")



