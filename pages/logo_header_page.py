from pages.base_page import BasePage
from locators.logo_header_page_locators import LogoHeaderPageLocators


class LogoHeaderPage(BasePage):

    #клик по лого и переключение на новую вкладку
    def click_by_logo_and_switch_to_new_tab(self, title):
        original_window = self.current_window_handle()
        self.click_element(LogoHeaderPageLocators.LOGO_YANDEX)
        self.wait_number_of_windows_to_be(2)

        window_handles = self.window_handles()
        for window_handle in window_handles:
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                break
        
        self.wait_title_is(title)

    #Title новой страницы
    def find_and_get_title_on_new_page(self):
        return self.get_title()
    
    #Клик по лого
    def find_and_click_by_logo(self, main_page):
        self.click_element(LogoHeaderPageLocators.LOGO_SCOOTER)
        self.wait_url_changes(main_page)

    #элемент на новой странице
    def find_and_get_element_on_new_page(self):
        return self.get_text_element(LogoHeaderPageLocators.SCOOTER_DISCLAIMER)
