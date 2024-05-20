import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium import webdriver
from pages.catalog.catalog_page_acc import Catalog_page_acc

driver = webdriver.Chrome()
cpc = Catalog_page_acc




class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    # Локатор кнопки перехода на страницу Корзина
    cart_button = "//a[@class='sh-basket-btn sh-basket__pending']"

    # Локатор проверочного слова на странице
    word = "//h1[@class='page-head__title nomobile']"

    # Локатор для определения названия карточки товара
    label_product = "(//div[@class='cart-prod__title'])"

    # Локатор для определения стоимости товара
    price = "(//div[@class='cart-prod__summ'])"

    # Локатор кнопки "Оформить заказ" на странице
    continue_button = "//button[@class='btn btn_green resume__final-btn']"

    # Текст оформить заказ на странице оформить заказ
    continue_text = "//h1[@class='page-head__title']"

    # Локатор кнопки "Удалить" товар из корзины на странице
    delete_product = "(//a[@class='cart-prod__close'])"

    # Локатор иконки логотипа на Главной странице
    logo = "//div[@class='sh-logo']"

    # Локатора проверочного слова пустой Корзины
    empty_cart = "//div[@class='nomobile']"



    """Getters"""
    # Getter локатора проверочного слова на странице Корзина
    def get_word(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.word)))

    # Getter локатора проверочного слова пустой корзины
    def get_empty_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.empty_cart)))

    # Getter локатора проверочного слвоа на странице офомить заказ
    def get_continue_word(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.continue_text)))

    # Getter кнопка перехода на страницу Корзина
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button)))


    def get_cart_product(self):
        cart_product = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.label_product)))
        return cart_product

    # Getter локатора кнопки "Оформить заказ" на странице Корзина
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Getter локатора кнопки "Удалить" 1 товар из корзины на странице Корзина
    def get_delete_product_1(self):
        del_cart_product_1 = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.delete_product)))
        return del_cart_product_1

    # Getter локатора кнопки "Удалить" 2 товар из корзины на странице Корзина
    def get_delete_product_2(self):
        del_cart_product_2 = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.delete_product)))
        return del_cart_product_2[1]


    # Getter стоимости певого выбранного товара на странице Корзина
    def get_label_price(self):
        label_price = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.price)))
        return label_price

    # Getter локатора иконки логотипа на Главной странице
    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.logo)))




    """Actions"""
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Переход на страницу корзина успешный")
        self.assert_word(self.get_word(), "Моя корзина")


    def text_cart_product_1(self):                              # Название первого товара в Корзине
        label = self.get_cart_product()
        self.cart_product = label[0].text
        print("Название выбранного товара: ", self.cart_product)
        return self.cart_product


    def print_price_1(self):                                    # Стоимость первого товара в Корзине
        price_getter = self.get_label_price()
        self.price_product = price_getter[0].text
        price = re.sub(r'\D', '', self.price_product)
        print("Стоимость выбранного товара: ", price + " рублей")
        self.price_product = price
        return self.price_product

    def print_price_2(self):                                    # Стоимость второго товара в Корзине
        price_getter = self.get_label_price()
        self.price_product = price_getter[1].text
        price = re.sub(r'\D', '', self.price_product)
        print("Стоимость выбранного товара: ", price + " рублей")
        self.price_product = price
        return self.price_product

    def text_cart_product_2(self):                              # Название второго товара в Корзине
        label = self.get_cart_product()
        self.cart_product = label[1].text
        print("Название выбранного товара: ", self.cart_product)
        return self.cart_product


    def click_continue_button(self):                            # Переход на страницу Оформление заказа
        self.get_continue_button().click()

    def click_logo(self):                                       # Переход на Главную страницу
        self.get_logo().click()
        print("Переход на Главную страницу")

    # Удаление первого товара из корзины
    def delete_product_1(self):
        self.get_delete_product_1().click()
        print("Товар удален из корзины")


    """Methods"""
    def e2e_cart(self):
        self.click_cart_button()                                # Переход на страницу Корзина

    def e2e_continue(self):
        self.click_continue_button()
        self.assert_word(self.get_continue_word(), "Оформление заказа")
        time.sleep(4)
        self.back_page()
        self.delete_product_1()
        self.delete_product_1()
        time.sleep(1)
        self.assert_word(self.get_empty_cart(), "В вашей корзине ещё нет товаров.")


    def return_main_page(self):
        self.scroll_page(0, 0)
        self.click_logo()
        self.assert_url("https://pitergsm.ru/")

