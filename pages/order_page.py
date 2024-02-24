from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    #скролл и нажатие на кнопку "Заказать"
    def scroll_and_click_to_order_button(self, button, header):
        self.scroll_to_element(button)
        self.wait_visible_element(button)
        self.click_element(button)
        self.wait_visible_element(header)

    #поиск и нажатие на элемент
    def find_and_click_button(self, button, header):
        self.click_element(button)
        self.wait_visible_element(header)

    #поиск и заполнение поля
    def find_and_fill_the_order_form(self, fill, text):
        self.find_element_and_type_text(fill, text)
    
    #клик по выпадающему списку и выбор пункта списка
    def find_and_chose_the_element(self, fill, search, chose, value):
        self.click_element(fill)
        self.wait_visible_element(search)
        locator_chose = self.format_locator(chose, value)
        self.click_element(locator_chose)

    #отметить чекбокс
    def find_and_chose_the_checkbox(self, checkbox, value):
        locator_checkbox = self.format_locator(checkbox, value)
        self.click_element(locator_checkbox)

    #заполнение первой формы заказа и нажатие на кнопку Далее
    def fill_the_first_oder_form(self, button_locator, name, surname, address, station, phone):
        self.scroll_and_click_to_order_button(
            button_locator, (OrderPageLocators.ORDER_FIRST_FORM))
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_NAME), name)
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_SURNAME), surname)
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_ADDRESS), address)
        self.find_and_chose_the_element(
            (OrderPageLocators.FILL_STATION), (OrderPageLocators.STATION_SEARCH), (OrderPageLocators.STATION_SELECT), station)
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_PHONE), phone)
        self.find_and_click_button(
            (OrderPageLocators.FIRST_FORM_NEXT_BUTTON), (OrderPageLocators.ORDER_SECOND_FORM))

    #заполнение второй формы заказа и нажатие кнопки Заказать
    def fill_the_second_order_form(self, date, duration, color, comment):
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_DATE), date)
        self.find_and_chose_the_element(
            (OrderPageLocators.FILL_DURATION), (OrderPageLocators.DURATION_SEARCH), (OrderPageLocators.DURATION_SELECT), duration)
        self.find_and_chose_the_checkbox(
            (OrderPageLocators.CHECKBOX_COLOR), color)
        self.find_and_fill_the_order_form(
            (OrderPageLocators.FILL_COMMENT), comment)
        self.find_and_click_button(
            (OrderPageLocators.SECOND_FORM_ORDER_BUTTON), (OrderPageLocators.ORDER_QUESTION))
    
    # нажатие на кнопку подтверждения и получение текста с высплювающего
    # окна успешного заказа
    def click_and_get_success_order_text(self):
        self.click_element((OrderPageLocators.ORDER_YES_BUTTON))
        result = self.get_text_element((OrderPageLocators.ORDER_SUCCESS))
        return result
