import pytest
from pages.faq_page import FaqPage
from data import answers


class TestFaqPage:

    @pytest.mark.parametrize('q_number, expected_answer', 
                             [
                                 [0, answers['answer_0']],
                                 [1, answers['answer_1']],
                                 [2, answers['answer_2']],
                                 [3, answers['answer_3']],
                                 [4, answers['answer_4']],
                                 [5, answers['answer_5']],
                                 [6, answers['answer_6']],
                                 [7, answers['answer_7']],
                            ])
    def test_faq_answer(self, browser, q_number, expected_answer):
        faq_page = FaqPage(browser)
        browser.get('https://qa-scooter.praktikum-services.ru/')
        faq_page.scroll_to_faq()
        result = faq_page.click_and_get_answer_text(q_number)
        assert expected_answer == result, f'Ожидаемый ответ "{expected_answer}" не соответствует действительному "{result}"'

