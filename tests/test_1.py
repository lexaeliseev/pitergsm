from base.base_class import Base
from pages.catalog.catalog_page_acc import Catalog_page_acc
from pages.catalog.catalog_page_certificate import Catalog_page_certificates
from pages.cart_page import Cart_page
import pytest
from pages.login_page import Login_page
from selenium import webdriver




def test_1():
    # Браузеры
    driver = webdriver.Chrome()                                         # для запуска с открытием окна браузера
    # driver = webdriver.Firefox()

    # Экземпляры класcов
    bp = Base(driver)                                                   # Базовый экземпляр класса
    lg = Login_page(driver)                                             # Класс авторизации
    cpc = Catalog_page_certificates(driver)                             # Класс страницы каталога Сертификаты
    cpa = Catalog_page_acc(driver)                                      # Класс страницы каталога Аксессуары
    cp = Cart_page(driver)                                              # Класс страницы Корзина

    # Авторизация
    lg.authorization()                                                  # Авторизация в системе
    # 1-ый товар
    cpa.e2e_product()                                                   # Работа с товаром ка странице Аксессуары
    # 2-ой товар
    cpc.e2e_product()                                                   # Работа с товаром ка странице Сертификаты
    # Корзина
    cp.e2e_cart()                                                       # Переход на страницу Корзина

    # Сравнение названия и стоимости первого добавленного товара и этого же товара на странице Корзина
    bp.assert_value(cpa.product_label, cp.text_cart_product_1())

    # Сравнение стоимости первого добавленного товара и этого же товара на странице Корзина
    bp.assert_price(cpa.price_product, cp.print_price_1())

    # Сравнение названия второго добавленного товара и этого же товара на странице Корзина
    bp.assert_value(cpc.product_label, cp.text_cart_product_2())

    # Сравнение стоимости второго добавленного товара и этого же товара на странице Корзина
    bp.assert_price(cpc.price, cp.print_price_2())

    cp.e2e_continue()                                                   # Переход на страницу Оформление заказа

    cp.return_main_page()                                               # Переход на Главную страницу сайта

    lg.driver.quit()                                                    # Закрытие браузера
















