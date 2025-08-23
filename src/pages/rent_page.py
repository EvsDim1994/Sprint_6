import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class RentPage:
    description_rent_window = (By.CLASS_NAME, "Order_Header__BZXOb")
    calendar = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    date = (By.XPATH, ".//div[text()='21']")
    duration_list = (By.XPATH, ".//div[text()='* Срок аренды']")
    duration = (By.XPATH, ".//div[text()='трое суток']")
    comment_field = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    submit_order_button = (By.XPATH, ".//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    yes_button = (By.XPATH, ".//button[text()='Да' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    description_confirm_order = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    @allure.step('Проверить переход на форму "Про аренд"')
    def ckeck_rent_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.description_rent_window))
        assert self.driver.find_element(*self.description_rent_window).text == "Про аренду"

    @allure.step('Выбор даты доставки')
    def select_date(self):
        self.driver.find_element(*self.calendar).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.date))
        self.driver.find_element(*self.date).click()

    @allure.step('Выбор срока аренды')
    def select_duration(self):
        self.driver.find_element(*self.duration_list).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.duration))
        self.driver.find_element(*self.duration).click()

    @allure.step('Выбор цвета')
    def select_color(self, color_name):
        color = (By.XPATH, f".//label[@for='{color_name}']")
        self.driver.find_element(*color).click()

    @allure.step('Ввод комментария')
    def input_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_submit_button(self):
        self.driver.find_element(*self.submit_order_button).click()

    @allure.step('Нажать на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Проверка оформления заказа')
    def check_order(self):
        assert WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(self.description_confirm_order, "Заказ оформлен"))

    