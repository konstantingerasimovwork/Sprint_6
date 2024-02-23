from selenium.webdriver.common.by import By

class FaqPageLocators:

    FAQ_ELEMENT = By.CLASS_NAME, 'Home_FAQ__3uVm4'
    ACCORDION_BUTTON = By.CSS_SELECTOR, 'accordion__button'
    ACCORDION_HEADING = By.ID, 'accordion__heading-{}'
    ACCORDION_PANEL = By.ID, 'accordion__panel-{}'
