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
        order_page.fill_the_first_oder_form(
            button_locator, name, surname, address, station, phone)
        order_page.fill_the_second_order_form(date, duration, color, comment)
        success_order_text = order_page.click_and_get_success_order_text()
        assert 'Заказ оформлен' in success_order_text, 'Не появилось всплывающее окно с сообщением об успешном создании заказа.'
