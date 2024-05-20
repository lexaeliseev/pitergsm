import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)


    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Значения: {value_word} и {result} совпадают!")


    """Method assert value"""

    def assert_value(self, text1, text2):
        assert text1 == text2
        print(f"Название товара с первой страницы: {text1} и с второй страницы: {text2} совпадают")

    """Method assert price"""

    def assert_price(self, price1, price2):
        assert price1 == price2
        print(f"Цена на странице товара {price1} и в корзине совпадают {price2}")

    """Method assert url"""
    def assert_url(self, result):
        assert self.driver.current_url == result
        print(f"Значения URL: {self.driver.current_url} и {result} совпадают!")

    """Method Screenshot"""
    def get_screenshot(self):
        self.get_current_url()
        now_date = datetime.datetime.now().strftime("%d.%m_%H:%M:%S.")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('/Users/aleksej/PycharmProjects/main_project/screen/' + name_screenshot)


    """Method Scroll Window"""
    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
        print("Скролл экрана")


    """Method Move to elements"""
    # Почитать подробнее про execute_script - сработал код с Stack OverFlow
    def move_to_element(self, driver, locator, index=0):
        try:
            element_locator = f'({locator})[{index}]'
            element = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, element_locator))
            )
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as e:
            print(f"Элемент {element_locator} не найден на странице: {e}")


    """Method Back Page"""
    def back_page(self):
        self.driver.back()
        print("Возврат на предыдущую страницу")















