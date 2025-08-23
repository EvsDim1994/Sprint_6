import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver



@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    # закрытие драйвера
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    # открыть главную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")