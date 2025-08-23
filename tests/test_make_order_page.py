import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.main_page import MainPageScooter

class TestMakeOrder:

    @pytest.mark.parametrize('name, surname, adress, phone, color_name, comment', 
        [
                [ "Дмитрий", "Евсюков", "Волгоградский проспект 21", "99990002323", "black", "Возле метро"],
                [ "Дмитрий", "Евсюков", "Волгоградский проспект 21", "99990002323", "grey", ""]
        ])
    def test_make_order_by_top_button(self, driver: WebDriver, 
                                      main_page, 
                                      name, 
                                      surname, 
                                      adress,
                                      phone, 
                                      color_name,
                                      comment):
        main_page = MainPageScooter(driver)

        main_page.click_cookie()

        for_who_scooter_page = main_page.click_order_top_button()

        for_who_scooter_page.check_for_who_scotter_page()

        for_who_scooter_page.input_name(name)

        for_who_scooter_page.input_surname(surname)

        for_who_scooter_page.input_adress(adress)

        for_who_scooter_page.select_station()

        for_who_scooter_page.input_phone(phone)

        rent_page = for_who_scooter_page.click_next_page_button()

        rent_page.select_date()

        rent_page.select_duration()

        rent_page.select_color(color_name)

        rent_page.input_comment(comment)

        rent_page.click_submit_button()

        rent_page.click_yes_button()

        rent_page.check_order()


    def test_make_order_by_down_button(self, driver: WebDriver, main_page):

        main_page = MainPageScooter(driver)

        main_page.click_cookie()

        for_who_scooter_page = main_page.click_order_down_button()

        for_who_scooter_page.check_for_who_scotter_page()

        for_who_scooter_page.input_name("Дмитрий")

        for_who_scooter_page.input_surname("Евсюков")

        for_who_scooter_page.input_adress("Волгоградский проспект 21н")

        for_who_scooter_page.select_station()

        for_who_scooter_page.input_phone("79884900639")

        rent_page = for_who_scooter_page.click_next_page_button()

        rent_page.select_date()

        rent_page.select_duration()

        rent_page.select_color("grey")

        rent_page.input_comment("комментарий")

        rent_page.click_submit_button()

        rent_page.click_yes_button()

        rent_page.check_order()
