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

    def click_order_top_button(self):
        self.driver.find_element(*self.make_order_top_button).click()
        return ForWhoScooterPage(self.driver)
    
    def click_order_down_button(self):
        self.driver.find_element(*self.make_order_down_button).click()
        return ForWhoScooterPage(self.driver)        
    