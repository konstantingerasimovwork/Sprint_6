from pages.base_page import BasePage


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

    #нажатие на кнопку подтверждения и получение текста с высплювающего
    #окна успешного заказа
    def click_and_get_success_order_text(self, button, header):
        self.click_element((button))
        result = self.get_text_element((header))
        return result

