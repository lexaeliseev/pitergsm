import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import re
from base.base_class import Base

class Catalog_page_acc(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.implicitly_wait(10)

    """Locators"""
    # Локатор для перехода на Главную страницу сайта
    icon_main = "//div[@class='sh-line__logo']"

    # Локатор для перехода в каталог Аксессуары
    icon_acc = "//a[@class='sh-menu__link accessories']"

    # Локатор проверочного слова на странице
    word = "//h1[@class='page-head__title']"

    # Локатор для определения названия карточки товара
    label_product = "(//div[@class='prod-card__title'])"

    # Локаторы для фильтров по стоимости
    price_from = "//input[@class='filter-input__field filter-input__field--from']"
    price_to = "//input[@class='filter-input__field filter-input__field--to']"

    # Локатор кнопки Купить товара на странице каталога
    select_product = "(//a[@class='btn btn_green prod-card__order product-buy-trigger'])"
    # select_product = "(//span[@class='product-buy-trigger__def'])"

    # Локатор кнопки купить на странице с товаром
    button_buy = "//div[@class='product-price__buy']"

    # Локатор кнопки "В корзину"
    add_product_catalog = "//a[@class='sh-basket-btn sh-basket__pending']"

    # Локатор кнопки продолжить покупки
    continue_shopping = "//a[@class='pop-cart__more']"

    """Assert Locators"""
    # Локатор стоимости на странице каталога
    assert_price = "(//div[@class='prod-card__price']/div[@class='price']/div[@class='price__now'])"

    # Локатор карточки товара
    card = "(//div[@class='prod-card__info-btm'])"


    """Getters"""

    # Getter локатора для перехода на Главную страницу
    def get_icon_main(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_main)))

    # Getter локаторa для перехода в каталог Аксессуары
    def get_icon_acc(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.icon_acc)))

    # Getter локатора проверочного слова на странице КАТАЛОГА Аксессуары
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

    # Getter товара в каталоге
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


    """Assert Getters"""
    # Getter локатора стоимости на странице каталога СЕРТИФИКАТЫ
    def get_assert_price(self):
        price_product = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.assert_price)))
        return price_product

    # Getter локатора названия на странице каталога СЕРТИФИКАТЫ
    def get_label_product(self):
        label_product = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.label_product)))
        return label_product


    """Action"""
    def click_button_icon_main(self):
        self.get_icon_main().click()
        self.assert_url("https://pitergsm.ru/")
        print("Переход на Главную страницу сайта")

    def click_button_acc(self):
        self.get_icon_acc().click()
        print("Переход на страницу Аксессуары")
        self.assert_url("https://pitergsm.ru/catalog/accessories/")
        self.assert_word(self.get_word(), "Аксессуары")

    def click_product(self):
        click = self.get_select_products()
        click[4].click()                                               # Клик по кнопке Купить 5-ого товара



    def print_price_1(self):                                            # Cтоимость 5-ого товара на странице
        price_getter = self.get_assert_price()
        self.price_product = price_getter[4].text
        price = re.sub(r'\D', '', self.price_product)
        print("Стоимость выбранного товара: ", price + " рублей")
        self.price_product = price
        return self.price_product


    def print_label_product_1(self):                                    # Название 5-ого товара на странице
        label = self.get_label_product()
        self.product_label = label[4].text
        print("Название выбранного товара: ", self.product_label)
        return self.product_label


    def click_button_cart(self):                                        # Добавление товара в Корзину
        self.get_button_to_cart().click()
        print("Выбранный товар добавлен в корзину")

    def click_button_continue_shopping(self):                           # Клик по кнопке Продолжение покупок
        self.get_button_continue_shopping().click()
        print("Товар добавлен в корзину, продолжение покупок.")

    def click_button_buy(self):                                         # Клик по кнопке Купить на странице с товаром
        self.get_button_bye().click()


    """Methods"""
    def e2e_product(self):                                          # Работа с 5 карточкой товара
        self.click_button_acc()                                     # Переход на страницу Аксессуары
        self.move_to_element(self.driver, self.select_product, 5)   # Перемещение к карточке 5 товара
        self.click_product()                                        # Клик по кнопке Купить
        self.click_button_buy()                                     # Добавление товара в корзину и продолжение покупок
        self.back_page()                                            # Возврат на предыдущую страницу
        self.print_label_product_1()                                # Отображение названия 5 товара
        self.print_price_1()                                        # Отображение стоимости 5 товара
        self.scroll_page(0, 0)                                      # Переход в шапку Сайта
        self.click_button_icon_main()                               # Клик по логотипу сайта

