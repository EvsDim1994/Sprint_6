import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.main_page import MainPageScooter

class TestMakeOrder:

    @pytest.mark.parametrize('button, name, surname, adress, phone, color_name, comment', 
        [
                [ "top_button","Дмитрий", "Евсюков", "Волгоградский проспект 21", "99990002323", "black", "Возле метро"],
                [ "down_button", "Дмитрий", "Евсюков", "Волгоградский проспект 21", "99990002323", "grey", ""]
        ])
    def test_make_order_button(self, driver: WebDriver, 
                                      main_page,
                                      button,
                                      name, 
                                      surname, 
                                      adress,
                                      phone, 
                                      color_name,
                                      comment):
        main_page = MainPageScooter(driver)
        # Нажатие на кпоку cookie
        main_page.click_cookie()
        # Нажатие на кнопку заказа самоката в зависимости от переданного параментра 
        for_who_scooter_page = main_page.click_order_button(button)
        # Заполнение формы Для кого самокат
        for_who_scooter_page.input_for_who_scooter_form(name, surname, adress, phone)
        # Переход к форме Про аренду
        rent_page = for_who_scooter_page.click_next_page_button()
        # Заполнение формы Про аренду
        rent_page.input_rent_form(color_name, comment)
        # Нажатие на кнопку Заказать
        rent_page.click_submit_button()
        # Нажатие на кнопку Да
        rent_page.click_yes_button()
        # Проверка оформления заказа
        rent_page.check_order()
        # Нажать на кпопку посмотреть статус заказа
        rent_page.click_show_order_button()
        # Нажатие на кнопку самокат
        main_page.click_scooter_button()
        # Проверка перехода на главную старницу
        main_page.check_main_page()
        # Нажатие на кпопку Яндекс
        main_page.click_yandex_button()
        # Проверка перехода на страницу dzen
        main_page.check_dzen_page()
        
