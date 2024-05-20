import time

from selenium.webdriver.chrome.options import Options

from pages.login_page import Login_page
from selenium import webdriver
import pytest

from pages.main_page import Main_page


def test_authorization():
    # options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    driver = webdriver.Chrome() # для запуска с открытием окна браузера

    print("Тест: проверка АВТОРИЗАЦИИ")
    lg = Login_page(driver)
    lg.authorization()


