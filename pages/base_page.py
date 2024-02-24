from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    #поиск элемента
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    #клик по элементу
    def click_element(self, locator):
        self.find_element(locator).click()
    
    #получить текст элемента
    def get_text_element(self, locator):
        return self.find_element(locator).text

    def get_title(self):
        return self.browser.title

    #ожидание появления элемента
    def wait_visible_element(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_url_changes(self, url):
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes(url))
    
    def wait_number_of_windows_to_be(self, number):
        WebDriverWait(self.browser, 5).until(expected_conditions.number_of_windows_to_be(number))

    def wait_title_is(self, title):
        WebDriverWait(self.browser, 9).until(expected_conditions.title_is(title))

    def current_window_handle(self):
        return self.browser.current_window_handle

    def window_handles(self):
        return self.browser.window_handles
    
    def switch_to_window(self, window_handle):
        return self.browser.switch_to.window(window_handle)

    #скролл до элемента
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    #Форматирование строки
    def format_locator(self, locator, value):
        method, locator = locator
        return method, locator.format(value)
    
    #ввод текста
    def find_element_and_type_text(self,locator, text):
        self.find_element(locator).send_keys(text)
        
