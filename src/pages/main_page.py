import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import driver
from src.pages.for_who_scooter_page import ForWhoScooterPage

class MainPageScooter:
    cookie = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    make_order_top_button = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    make_order_down_button = (By.CLASS_NAME, "Button_Middle__1CSJM")
    scooter_button = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    description_main_page_window = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    yandex_button = (By.XPATH, ".//img[@alt='Yandex']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на кнопку cookie')
    def click_cookie(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.cookie))
        self.driver.find_element(*self.cookie).click()

    @allure.step('Нажать на вопрос')
    def click_question_button(self, index_question):
        question = (By.XPATH, f".//div[@id='accordion__heading-{index_question}']")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question)) 
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    @allure.step('Проверить ответ на вопрос')
    def check_question(self, index_answer, text):
        question_text = (By.ID, f"accordion__panel-{index_answer}")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(question_text))
        assert self.driver.find_element(*question_text).text == text

    def click_order_button(self, button):
        if button == "top_button":
            self.driver.find_element(*self.make_order_top_button).click()
        elif button == "down_button":
            self.driver.find_element(*self.make_order_down_button).click()
        return ForWhoScooterPage(self.driver)

    @allure.step('Нажать на кнопку самокат')
    def click_scooter_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.scooter_button))
        self.driver.find_element(*self.scooter_button).click()

    @allure.step('Проверка перехода на главную страницу')
    def check_main_page(self):
        assert WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(self.description_main_page_window, "Самокат\nна пару дней"))

    @allure.step('Нажать на кнопку Яндекс')
    def click_yandex_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.yandex_button))
        self.driver.find_element(*self.yandex_button).click()

    @allure.step('Проверка перехода на страницу https://dzen.ru/?yredirect=true')
    def check_dzen_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        new_windows = self.driver.window_handles
        self.driver.switch_to.window(new_windows[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be("https://dzen.ru/?yredirect=true"))
        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"
        