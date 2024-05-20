import re
import time

import self as self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Catalog_page_certificates(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    card = "(//div[@class='prod-card__info-btm'])"



    # Локатор кнопки "В корзину"
    add_product_catalog = "//a[@class='btn btn_green btn_txt-big']"
    # Локатор кнопки продолжить покупки
    continue_shopping = "//a[@class='pop-cart__more']"

    """Assert Locators"""
    # Локатор стоимости на странице каталога Сертификаты
    assert_price = "(//div[@class='prod-card__price']/div[@class='price']/div[@class='price__now'])"

    # Локатор поля ПОИСК на Главной странице
    search = "//input[@id='smart-title-search-input']"

    """Getters"""
    # Getter локатора для перехода на Главную страницу
    def get_icon_main(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_main)))

    # Getter локаторa для перехода в каталог Сертификаты
    def get_icon_certificate(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_certificate)))

    # Getter локатора проверочного слова на странице КАТАЛОГА СЕРТИФИКАТЫ
    def get_word(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.word)))

    # Getters локаторов для фильтров по стоимости
    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.price_to)))

    # GETTER ЛОКАТОРА КНОПКИ "КУПИТЬ" У ТРЕТЬЕЙ КАРТОЧКИ ТОВАРА
    def get_select_products(self):
        product = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.select_product)))
        return product

    # Getter кнопки Купить на странице товара
    def get_button_bye(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_buy)))

    # GETTER ЛОКАТОРА КНОПКИ "В КОРЗИНУ" В МОДАЛЬНОМ ОКНЕ КАРТОЧКИ ТОВАРА
    def get_button_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_product_catalog)))

    # GETTER ЛОКАТОРА КНОПКИ "ПРОДОЛЖИТЬ ПОКУПКИ В МОДАЛЬНОМ ОКНЕ КАРТОЧКИ ТОВАРА
    def get_button_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.continue_shopping)))

    # Getter локатора поля ПОИСК на Главной странице
    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search)))


    """Assert Getters"""
    # Getter локатора стоимости на странице каталога СЕРТИФИКАТЫ - ТРЕТЬЯ карточка товара
    def get_assert_price(self):
        price_product = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.assert_price)))
        return price_product

    # Getter локатора названия на странице каталога СЕРТИФИКАТЫ - ТРЕТЬЯ карточка товара
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

    def print_price(self):                                      # Стоимость выбранного товара на странице
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

    # Клик по кнопке Купить на странице с товаром
    def click_button_buy(self):
        self.get_button_bye().click()

    # ФИЛЬТРЫ - не работаеют на сайте
    def filters(self):
        self.get_price_from().send_keys(Keys.BACKSPACE*10)
        self.get_price_from().send_keys("15000")
        self.get_price_to().send_keys(Keys.BACKSPACE*10)
        self.get_price_to().send_keys("15000")
        time.sleep(1)



    # НЕ РАБОТАЕТ ПОИСК НА САЙТЕ НА МОМЕНТ НАПИСАНИЯ АТК
    def enter_search(self):
        self.get_input_search().click()
        self.get_input_search().send_keys("Сертификат")
        self.get_input_search().send_keys(Keys.ENTER)
        self.scroll_page(0, 150)
        print("Поиск отработал корректно!")

    """Methods"""
    def e2e_product(self):
        self.click_button_certificates()                            # Переход на страницу Сертификаты
        self.move_to_element(self.driver, self.select_product, 4)   # Перемещение к карточке товара
        self.click_product()                                        # Клик по кнопке "Купить" у 3 товара
        self.click_button_buy()                                     # Клик по кнопке "Купить"
        self.back_page()                                            # Возврат на предыдущую страницу
        self.print_label_product_2()                                # Отображение названия 3 товара
        self.print_price()                                          # Отображение стоимости 3 товара
        self.scroll_page(0, 0)                                      # Переход в шапку Сайта
        self.click_button_icon_main()                               # Клик по логотипу сайта
