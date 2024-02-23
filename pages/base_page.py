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

    #ожидание появления элемента
    def wait_visible_element(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))
    
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
        
