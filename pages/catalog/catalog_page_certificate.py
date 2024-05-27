import re
import time

import allure
import self as self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Catalog_page_certificates(Base):


    """Locators"""
    # Локатор для перехода на Главную страницу сайта
    icon_main = "//div[@class='sh-line__logo']"

    # Локатор для перехода в каталог Сертификаты
    icon_certificate = "//a[@class='sh-menu__link certificates']"

    # Локатор проверочного слова на странице Сертификаты
    word = "//h1[@class='page-head__title']"

    # Локатор для определения названия карточки товара
    label_product = "(//div[@class='prod-card__title'])"

    # Локаторы для фильтров по стоимости
    price_from = "//input[@class='filter-input__field filter-input__field--from']"
    price_to = "//input[@class='filter-input__field filter-input__field--to']"

    # Локатор карточки товара на странице каталога СЕРТИФИКАТЫ
    # select_product = "(//a[@class='btn btn_green prod-card__order product-buy-trigger'])"
    select_product = "(//a[@class='btn btn_green prod-card__order product-buy-trigger'])"

    # Локатор кнопки купить на странице с товаром
    button_buy = "(//div[@class='product-price__buy'])"

    # Локатор карточки товара
    card = "(//div[@class='prod-card__info-btm'])"

    # Локатор кнопки "В корзину"
    add_product_catalog = "//a[@class='btn btn_green btn_txt-big']"

    # Локатор кнопки "Продолжить покупки"
    continue_shopping = "//a[@class='pop-cart__more']"

    """Assert Locators"""
    # Локатор стоимости на странице каталога Сертификаты
    assert_price = "(//div[@class='prod-card__price']/div[@class='price']/div[@class='price__now'])"

    # Локатор поля ПОИСК на Главной странице
    search = "//input[@id='smart-title-search-input']"

    """Getters"""
    def get_icon_main(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_main)))

    def get_icon_certificate(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_certificate)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.word)))

    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.price_to)))

    def get_select_products(self):
        product = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.select_product)))
        return product

    def get_button_bye(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_product_catalog)))

    def get_button_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.continue_shopping)))

    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search)))

    def get_assert_price(self):
        price_product = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.assert_price)))
        return price_product

    def get_label_product(self):
        label_product = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.label_product)))
        return label_product

    """Action"""

    def click_button_icon_main(self):
        self.get_icon_main().click()
        self.assert_url("https://pitergsm.ru/")
        print("Переход на Главную страницу сайта")

    def click_button_certificates(self):
        self.get_icon_certificate().click()
        print("Переход на страницу Сертификаты")
        self.assert_url("https://pitergsm.ru/catalog/certificates/")
        self.assert_word(self.get_word(), "Сертификаты")

    def click_product(self):
        click = self.get_select_products()
        click[3].click()

    def print_price(self):                                         # Стоимость выбранного товара на странице
        price_getter = self.get_assert_price()
        price_product = price_getter[3].text
        price = re.sub(r'\D', '', price_product)
        print("Стоимость выбранного товара: ", price + " рублей")
        self.price = price
        return price

    def print_label_product_2(self):                              # Название выбранного товара на странице
        label = self.get_label_product()
        product_label = label[3].text
        print("Название выбранного товара: ", product_label)
        self.product_label = product_label
        return product_label

    def click_button_cart(self):
        self.get_button_to_cart().click()
        print("Выбранный товар добавлен в корзину")

    def click_button_continue_shopping(self):
        self.get_button_continue_shopping().click()
        print("Товар добвлен в корзину, продолжение покупок.")

    def click_button_buy(self):
        self.get_button_bye().click()

    def filters(self):
        self.get_price_from().send_keys(Keys.BACKSPACE*10)
        self.get_price_from().send_keys("15000")
        self.get_price_to().send_keys(Keys.BACKSPACE*10)
        self.get_price_to().send_keys("15000")
        time.sleep(1)



    def enter_search(self):
        self.get_input_search().click()
        self.get_input_search().send_keys("Сертификат")
        self.get_input_search().send_keys(Keys.ENTER)
        self.scroll_page(0, 150)
        print("Поиск отработал корректно!")

    """Methods"""
    def e2e_product(self):
        with allure.step("e2e_product"):
            Logger.add_start_step(method="e2e_product")
            self.click_button_certificates()
            self.move_to_element(self.driver, self.select_product, 4)
            self.click_product()
            self.click_button_buy()
            self.back_page()
            self.print_label_product_2()
            self.print_price()
            self.scroll_page(0, 0)
            self.click_button_icon_main()
            Logger.add_end_step(url=self.driver.current_url, method="e2e_product")

