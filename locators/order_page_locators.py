from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_HEADER_BUTTON = By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g"]'
    ORDER_FINISH_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button'
    ORDER_FIRST_FORM = By.XPATH, './/div[text()="Для кого самокат"]'
    ORDER_SECOND_FORM = By.XPATH, './/div[text()="Про аренду"]'
    FIRST_FORM_NEXT_BUTTON = By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button[text()="Далее"]'
    SECOND_FORM_ORDER_BUTTON = By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'
    FILL_NAME = By.XPATH, './/input[@placeholder="* Имя"]'
    FILL_SURNAME = By.XPATH, './/input[@placeholder="* Фамилия"]'
    FILL_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    FILL_STATION = By.XPATH, './/input[@placeholder="* Станция метро"]'
    STATION_SEARCH = By.CLASS_NAME, 'select-search__select'
    STATION_SELECT = By.XPATH, './/div[text()="{}"]'
    FILL_PHONE = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'
    FILL_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]'
    FILL_DURATION = By.CLASS_NAME, 'Dropdown-arrow'
    DURATION_SEARCH = By.CLASS_NAME, 'Dropdown-menu'
    DURATION_SELECT = By.XPATH, './/div[text()="{}"]'
    CHECKBOX_COLOR = By.ID, '{}'
    FILL_COMMENT = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'
    ORDER_QUESTION = By.XPATH, './/div[text()="Хотите оформить заказ?"]'
    ORDER_YES_BUTTON = By.XPATH, './/button[text()="Да"]'
    ORDER_SUCCESS = By.XPATH, './/div[text()="Заказ оформлен"]'

