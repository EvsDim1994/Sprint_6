from re import S
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.pages.base_page import BasePage

class RentPage(BasePage):
    DESCRIPTION_RENT_WINDOW = (By.CLASS_NAME, "Order_Header__BZXOb")
    CALENDAR = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE = (By.XPATH, ".//div[text()='21']")
    DURATION_LIST = (By.XPATH, ".//div[text()='* Срок аренды']")
    DURATION = (By.XPATH, ".//div[text()='трое суток']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH, ".//button[text()='Да' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    DESCRIPTION_CONFIRM_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    @allure.step('Проверить переход на форму "Про аренд"')
    def check_rent_page(self):
        self.waiting_visibility_element(self.DESCRIPTION_RENT_WINDOW)
        assert self.find_element(self.DESCRIPTION_RENT_WINDOW).text == "Про аренду"

    @allure.step('Выбор даты доставки')
    def select_date(self):
        self.click(self.CALENDAR)
        self.waiting_clickable(self.DATE)
        self.click(self.DATE)

    @allure.step('Выбор срока аренды')
    def select_duration(self):
        self.click(self.DURATION_LIST)
        self.waiting_clickable(self.DURATION)
        self.click(self.DURATION)

    @allure.step('Выбор цвета')
    def select_color(self, color_name):
        color = (By.XPATH, f".//label[@for='{color_name}']")
        self.click(color)

    @allure.step('Ввод комментария')
    def input_comment(self, comment):
        self.input_text(self.COMMENT_FIELD, comment)

    @allure.step('Заполнение формы про аренду')
    def input_rent_form(self, color_name, comment):
        self.check_rent_page()
        self.select_date()
        self.select_duration()
        self.select_color(color_name)
        self.input_comment(comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_submit_button(self):
        self.click(self.SUBMIT_ORDER_BUTTON)

    @allure.step('Нажать на кнопку "Да"')
    def click_yes_button(self):
        self.click(self.YES_BUTTON)

    @allure.step('Проверка оформления заказа')
    def check_order(self):
        assert self.waiting_text_in_element(self.DESCRIPTION_CONFIRM_ORDER, "Заказ оформлен")

    @allure.step('Нажать на кнопку "Посмотреть статус"')
    def click_show_order_button(self):
        self.click(self.STATUS_BUTTON)
        