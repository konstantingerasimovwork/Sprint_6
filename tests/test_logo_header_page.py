from pages.logo_header_page import LogoHeaderPage
from locators.logo_header_page_locators import LogoHeaderPageLocators


class TestLogoHeaderPage:

    def test_yandex_logo(self, browser):
        logo = LogoHeaderPage(browser)
        browser.get('https://qa-scooter.praktikum-services.ru/order')
        logo.click_by_logo_and_switch_to_new_tab((LogoHeaderPageLocators.LOGO_YANDEX), 'Дзен')
        current_title = logo.find_and_get_title_on_new_page()
        assert current_title == 'Дзен', f'Title страницы "{current_title}"'


    def test_scooter_logo(self, browser):
        logo = LogoHeaderPage(browser)
        browser.get('https://qa-scooter.praktikum-services.ru/order')
        logo.find_and_click_by_logo(
            (LogoHeaderPageLocators.LOGO_SCOOTER), 'https://qa-scooter.praktikum-services.ru')
        # logo.click_by_logo_and_switch_to_new_tab(
        #     (LogoHeaderPageLocators.LOGO_SCOOTER), 'undefined')
        scooter_disclaimer = logo.find_and_get_element_on_new_page(LogoHeaderPageLocators.SCOOTER_DISCLAIMER)
        assert scooter_disclaimer == 'УЧЕБНЫЙ ТРЕНАЖЕР', f'Дисклеймер страницы "{scooter_disclaimer}"'
