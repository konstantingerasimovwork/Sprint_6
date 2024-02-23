from pages.base_page import BasePage

class FaqPage(BasePage):

    #скролл до выпадающего списка
    def scroll_to_faq(self, locator):
        self.scroll_to_element(locator)
        self.wait_visible_element(locator)

    #клик по элементу списка и получение текста ответа
    def click_and_get_answer_text(self, locator_q, locator_a, number):
        locator_q = self.format_locator(locator_q, number)
        locator_a = self.format_locator(locator_a, number)
        self.click_element((locator_q))
        self.wait_visible_element(locator_a)
        result = self.get_text_element((locator_a))
        return result
