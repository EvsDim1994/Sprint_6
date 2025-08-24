import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test

from conftest import driver
from src.pages.base_page import BasePage
from src.pages.for_who_scooter_page import ForWhoScooterPage

class MainPageScooter(BasePage):
    COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    MAKE_ORDER_TOP_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    MAKE_ORDER_DOWN_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")
    SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    DESCRIPTION_MAIN_PAGE_WINDOW = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    YANDEX_BUTTON = (By.XPATH, ".//img[@alt='Yandex']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на кнопку cookie')
    def click_cookie(self):
        self.waiting_visibility_element(self.COOKIE)
        self.click(self.COOKIE)

    @allure.step('Нажать на вопрос')
    def click_question_button(self, index_question):
        question = (By.XPATH, f".//div[@id='accordion__heading-{index_question}']")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question))
        self.waiting_clickable(question)
        self.click(question)

    @allure.step('Проверить ответ на вопрос')
    def check_question(self, index_answer, text):
        question_text = (By.ID, f"accordion__panel-{index_answer}")
        self.waiting_visibility_element(question_text)
        assert self.find_element(question_text).text == text

    def click_order_button(self, button):
        if button == "top_button":
            self.click(self.MAKE_ORDER_TOP_BUTTON)
        elif button == "down_button":
            self.click(self.MAKE_ORDER_DOWN_BUTTON)
        return ForWhoScooterPage(self.driver)

    @allure.step('Нажать на кнопку самокат')
    def click_scooter_button(self):
        self.waiting_visibility_element(self.SCOOTER_BUTTON)
        self.click(self.SCOOTER_BUTTON)

    @allure.step('Проверка перехода на главную страницу')
    def check_main_page(self):
        assert self.waiting_text_in_element(self.DESCRIPTION_MAIN_PAGE_WINDOW, "Самокат\nна пару дней")

    @allure.step('Нажать на кнопку Яндекс')
    def click_yandex_button(self):
        self.waiting_visibility_element(self.YANDEX_BUTTON)
        self.click(self.YANDEX_BUTTON)

    @allure.step('Проверка перехода на страницу https://dzen.ru/?yredirect=true')
    def check_dzen_page(self):
        self.waiting_windows_number(2)
        new_windows = self.driver.window_handles
        self.driver.switch_to.window(new_windows[-1])
        self.waiting_url("https://dzen.ru/?yredirect=true")
        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"
        