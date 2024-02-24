from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_HEADER_BUTTON = By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g"]' #Кнопка "Заказать" в хедере
    ORDER_FINISH_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button' #Кнопка "Заказать" в конце страницы
    ORDER_FIRST_FORM = By.XPATH, './/div[text()="Для кого самокат"]' #первая часть формы заказа
    ORDER_SECOND_FORM = By.XPATH, './/div[text()="Про аренду"]' #вторая часть формы заказа
    FIRST_FORM_NEXT_BUTTON = By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button[text()="Далее"]' #Кнопка "Далее" в первой части формы заказа
    SECOND_FORM_ORDER_BUTTON = By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]' #Кнопка "Заказать" во второй части формы заказа
    FILL_NAME = By.XPATH, './/input[@placeholder="* Имя"]' #Поле Имя
    FILL_SURNAME = By.XPATH, './/input[@placeholder="* Фамилия"]' #Поле Фамилия
    FILL_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]' # Поле Адрес
    FILL_STATION = By.XPATH, './/input[@placeholder="* Станция метро"]' # Поле Станция
    STATION_SEARCH = By.CLASS_NAME, 'select-search__select' # Выпадающий список поля Станция
    STATION_SELECT = By.XPATH, './/div[text()="{}"]' # Станция
    FILL_PHONE = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]' # Поле Телефон
    FILL_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]' # Поле Дата
    FILL_DURATION = By.CLASS_NAME, 'Dropdown-arrow' # Поле Срок аренды
    DURATION_SEARCH = By.CLASS_NAME, 'Dropdown-menu' # Выпадающий список поля Срок аренды
    DURATION_SELECT = By.XPATH, './/div[text()="{}"]' # Пункт поля срок аренды
    CHECKBOX_COLOR = By.ID, '{}' # Чекбокс
    FILL_COMMENT = By.XPATH, './/input[@placeholder="Комментарий для курьера"]' # Поле Комментарий
    ORDER_QUESTION = By.XPATH, './/div[text()="Хотите оформить заказ?"]'  # Заголовок всплывающего окна "Хотите оформить заказ?"
    ORDER_YES_BUTTON = By.XPATH, './/button[text()="Да"]' # Кнопка Да всплывающего окна "Хотите оформить заказ?"
    ORDER_SUCCESS = By.XPATH, './/div[text()="Заказ оформлен"]' # Заголовок всплывающего окна "Заказ оформлен"

