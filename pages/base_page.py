import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('скролл и нажатие на кнопку "Заказать"')
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    @allure.step('клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()
    
    @allure.step('получить текст элемента')
    def get_text_element(self, locator):
        return self.find_element(locator).text

    @allure.step('получить текст title')
    def get_title(self):
        return self.browser.title

    @allure.step('ожидание появления элемента')
    def wait_visible_element(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step('ожидание изменения url')
    def wait_url_changes(self, url):
        WebDriverWait(self.browser, 5).until(expected_conditions.url_changes(url))
    
    @allure.step('ожидание, что кол-во вкладок равняется заданному числу')
    def wait_number_of_windows_to_be(self, number):
        WebDriverWait(self.browser, 5).until(expected_conditions.number_of_windows_to_be(number))

    @allure.step('ожидание, что title равен заданному')
    def wait_title_is(self, title):
        WebDriverWait(self.browser, 9).until(expected_conditions.title_is(title))

    @allure.step('получение выбранной в настоящий момент вкладки')
    def current_window_handle(self):
        return self.browser.current_window_handle

    @allure.step('получаем все вкладки')
    def window_handles(self):
        return self.browser.window_handles
    
    @allure.step('переключение на нужную вкладку')
    def switch_to_window(self, window_handle):
        return self.browser.switch_to.window(window_handle)

    @allure.step('скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('форматирование строки')
    def format_locator(self, locator, value):
        method, locator = locator
        return method, locator.format(value)
    
    @allure.step('ввод текста')
    def find_element_and_type_text(self,locator, text):
        self.find_element(locator).send_keys(text)
        
