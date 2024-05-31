from selenium import webdriver
import pytest
import allure
from pages.login_page import Login_page
from base.base_class import Base
from pages.catalog.catalog_page_acc import Catalog_page_acc
from pages.catalog.catalog_page_certificate import Catalog_page_certificates
from pages.cart_page import Cart_page

@allure.description("test_smoke - добавление товара в корзину со страницы каталога, сравнение, что товар на странице корзина остался прежним и удаление товара из корзины")
def test_smoke():
    # Браузеры
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()

    # Экземпляры класcов
    bp = Base(driver)
    lg = Login_page(driver)
    cpc = Catalog_page_certificates(driver)
    cpa = Catalog_page_acc(driver)
    cp = Cart_page(driver)

    # Авторизация
    lg.authorization()
    # 1-ый товар
    cpa.e2e_product()
    # 2-ой товар
    cpc.e2e_product()
    # Корзина
    cp.e2e_cart()

    # Сравнение названия и стоимости первого добавленного товара и этого же товара на странице Корзина
    bp.assert_value(cpa.product_label, cp.text_cart_product_1())

    # Сравнение стоимости первого добавленного товара и этого же товара на странице Корзина
    bp.assert_price(cpa.price_product, cp.print_price_1())

    # Сравнение названия второго добавленного товара и этого же товара на странице Корзина
    bp.assert_value(cpc.product_label, cp.text_cart_product_2())

    # Сравнение стоимости второго добавленного товара и этого же товара на странице Корзина
    bp.assert_price(cpc.price, cp.print_price_2())

    # Переход на страницу Оформление заказа
    cp.e2e_continue()

    # Переход на Главную страницу сайта
    cp.return_main_page()

    # Закрытие браузера
    lg.driver.quit()
