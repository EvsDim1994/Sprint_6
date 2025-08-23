import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.pages.rent_page import RentPage

class ForWhoScooterPage:
    name_field = (By.XPATH, ".//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_field = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_list = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    station = (By.XPATH, ".//button[@value='4']")
    phone_field = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    description_for_who_scooter_window = (By.CLASS_NAME, "Order_Header__BZXOb")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Проверить переход на форму "Для кого самокат"')
    def check_for_who_scotter_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.description_for_who_scooter_window))
        assert self.driver.find_element(*self.description_for_who_scooter_window).text == "Для кого самокат"

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Ввод адреса')
    def input_adress(self, adress):
        self.driver.find_element(*self.adress_field).send_keys(adress)

    @allure.step('Выбор станции')
    def select_station(self):
        self.driver.find_element(*self.metro_list).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.station))
        self.driver.find_element(*self.station).click()

    @allure.step('Ввод номера телефона')
    def input_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

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
        self.driver.find_element(*self.next_button).click()
        return RentPage(self.driver)
    
        
    