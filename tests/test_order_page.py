import pytest
from pages.order_page import OrderPage
from data import order_first, order_second
from locators.order_page_locators import OrderPageLocators


class TestOrderPage():

    @pytest.mark.parametrize('button_locator, name, surname, address, station, phone, date, duration, color, comment',
                             [
                                 [OrderPageLocators.ORDER_HEADER_BUTTON, order_first['name'], order_first['surname'],
                                  order_first['address'],order_first['station'],
                                  order_first['phone'],order_first['date'],
                                  order_first['duration'], order_first['color'],
                                  order_first['comment'],
                                  ],
                                  [OrderPageLocators.ORDER_FINISH_BUTTON, order_second['name'], order_second['surname'],
                                  order_second['address'], order_second['station'],
                                  order_second['phone'], order_second['date'],
                                  order_second['duration'], order_second['color'],
                                  order_second['comment'],
                                  ]
                             ])
    def test_success_order(self, browser, button_locator, name, surname, address, station, phone, date, duration, color, comment):
        order_page = OrderPage(browser)
        browser.get('https://qa-scooter.praktikum-services.ru/')
        order_page.scroll_and_click_to_order_button(button_locator, (OrderPageLocators.ORDER_FIRST_FORM))
        order_page.find_and_fill_the_order_form((OrderPageLocators.FILL_NAME), name)
        order_page.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_SURNAME), surname)
        order_page.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_ADDRESS), address)
        order_page.find_and_chose_the_element(
            (OrderPageLocators.FILL_STATION), (OrderPageLocators.STATION_SEARCH), (OrderPageLocators.STATION_SELECT), station)
        order_page.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_PHONE), phone)
        order_page.find_and_click_button(
            (OrderPageLocators.FIRST_FORM_NEXT_BUTTON), (OrderPageLocators.ORDER_SECOND_FORM))
        order_page.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_DATE), date)
        order_page.find_and_chose_the_element(
            (OrderPageLocators.FILL_DURATION), (OrderPageLocators.DURATION_SEARCH), (OrderPageLocators.DURATION_SELECT), duration)
        order_page.find_and_chose_the_checkbox(
            (OrderPageLocators.CHECKBOX_COLOR), color)
        order_page.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_COMMENT), comment)
        order_page.find_and_click_button(
            (OrderPageLocators.SECOND_FORM_ORDER_BUTTON), (OrderPageLocators.ORDER_QUESTION))
        success_order_text = order_page.click_and_get_success_order_text((OrderPageLocators.ORDER_YES_BUTTON), (OrderPageLocators.ORDER_SUCCESS))
        assert 'Заказ оформлен' in success_order_text, 'Не появилось всплывающее окно с сообщением об успешном создании заказа.'
