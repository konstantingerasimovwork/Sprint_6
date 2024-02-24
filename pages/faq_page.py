import allure
from pages.base_page import BasePage
from locators.faq_page_locators import FaqPageLocators

class FaqPage(BasePage):

    @allure.step('скролл до выпадающего списка')
    def scroll_to_faq(self):
        self.scroll_to_element(FaqPageLocators.FAQ_ELEMENT)
        self.wait_visible_element(FaqPageLocators.FAQ_ELEMENT)

    @allure.step('клик по элементу списка и получение текста ответа')
    def click_and_get_answer_text(self, number):
        locator_q = self.format_locator(
            FaqPageLocators.ACCORDION_HEADING, number)
        locator_a = self.format_locator(
            FaqPageLocators.ACCORDION_PANEL, number)
        self.click_element((locator_q))
        self.wait_visible_element(locator_a)
        result = self.get_text_element((locator_a))
        return result
