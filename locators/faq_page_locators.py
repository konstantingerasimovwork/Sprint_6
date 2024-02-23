from selenium.webdriver.common.by import By

class FaqPageLocators:

    FAQ_ELEMENT = By.CLASS_NAME, 'Home_FAQ__3uVm4' #блок с вопросами и ответами
    ACCORDION_BUTTON = By.CSS_SELECTOR, 'accordion__button' #стрелка-кнопка, открывающая ответ
    ACCORDION_HEADING = By.ID, 'accordion__heading-{}' #блок с вопросом
    ACCORDION_PANEL = By.ID, 'accordion__panel-{}'  # блок с ответом
