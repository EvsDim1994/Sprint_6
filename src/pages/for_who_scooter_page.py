from re import S
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.pages.base_page import BasePage
from src.pages.rent_page import RentPage

class ForWhoScooterPage(BasePage):
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_LIST = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    STATION = (By.XPATH, ".//button[@value='4']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DESCRIPTION_FOR_WHO_SCOOTER_WINDOW = (By.CLASS_NAME, "Order_Header__BZXOb")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Проверить переход на форму "Для кого самокат"')
    def check_for_who_scotter_page(self):
        self.waiting_visibility_element(self.DESCRIPTION_FOR_WHO_SCOOTER_WINDOW)
        assert self.find_element(self.DESCRIPTION_FOR_WHO_SCOOTER_WINDOW).text == "Для кого самокат"

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.input_text(self.NAME_FIELD, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.input_text(self.SURNAME_FIELD, surname)

    @allure.step('Ввод адреса')
    def input_adress(self, adress):
        self.input_text(self.ADDRESS_FIELD, adress)

    @allure.step('Выбор станции')
    def select_station(self):
        self.click(self.METRO_LIST)
        self.waiting_clickable(self.STATION)
        self.click(self.STATION)

    @allure.step('Ввод номера телефона')
    def input_phone(self, phone):
        self.input_text(self.PHONE_FIELD, phone)

    @allure.step('Заполнение формы "Для кого самокат"')
    def input_for_who_scooter_form(self, name, surname, adress, phone):
        self.check_for_who_scotter_page()
        self.input_name(name)
        self.input_surname(surname)
        self.input_adress(adress)
        self.select_station()
        self.input_phone(phone)

    @allure.step('Нажатие на кнопку "Далее')
    def click_next_page_button(self):
        self.click(self.NEXT_BUTTON)
        return RentPage(self.driver)
    
        
    