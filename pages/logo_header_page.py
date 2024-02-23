from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage



class LogoHeaderPage(BasePage):

    #клик по лого и переключение на новую вкладку
    def click_by_logo_and_switch_to_new_tab(self, locator, title):
        original_window = self.browser.current_window_handle
        self.click_element(locator)
        WebDriverWait(self.browser, 5).until(expected_conditions.number_of_windows_to_be(2))


        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

        WebDriverWait(self.browser, 9).until(expected_conditions.title_is(title))

    #Title новой страницы
    def find_and_get_title_on_new_page(self):
        return self.browser.title
    
    #Клик по лого
    def find_and_click_by_logo(self, locator, main_page):
        self.click_element(locator)
        WebDriverWait(self.browser, 5).until(expected_conditions.url_changes(main_page))

    #элемент на новой странице
    def find_and_get_element_on_new_page(self, disclaimer_scooter):
        return self.get_text_element(disclaimer_scooter)
