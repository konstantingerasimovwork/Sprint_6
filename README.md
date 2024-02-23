# Sprint_6
### Предварительные требования
* Python 3.11
* pytest
* Selenium
* GeckoDriver для Firefox
* GeckoDriverManager

### Запуск тестов
* pytest -v
* pytest -v tests/test_faq_page.py
* pytest -v tests/test_order_page.py
* pytest -v tests/test_logo_header_page.py

Тесты запускаются для сайта https://qa-scooter.praktikum-services.ru/

### Дополнительные файлы
* data.py - тестовые данные для тестов
* conftest.py - фикстуры
* allure_results - результаты тестов

### Описания тестов
#### test_faq_page (Проверка выпадающего списка в разделе «Вопросы о важном»)
* test_faq_answer - проверка совпадения ответов

#### test_order_page (Проверка заказа самоката) 
* test_success_order - успешный заказ самоката

#### test_logo_header_page (Проверка логотипов в хедере)
* test_yandex_logo - при нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
* test_scooter_logo - при нажатии на логотип «Самоката», попадёшь на главную страницу «Самоката»


### Описания page object
#### faq_page (методы для test_faq_page) 
* scroll_to_faq - скролл до выпадающего списка
* find_and_click_button - клик по элементу списка и получение текста ответа

#### order_page (методы для test_order_page) 
* scroll_and_click_to_order_button - скролл и нажатие на кнопку "Заказать"
* find_and_click_button - поиск и нажатие на элемент
* find_and_fill_the_order_form - поиск и заполнение поля
* find_and_chose_the_element - клик по выпадающему списку и выбор пункта списка
* find_and_chose_the_checkbox - отметить чекбокс
* click_and_get_success_order_text - нажатие на кнопку подтверждения и получение текста с высплювающего окна успешного заказа

#### logo_header_page (методы для test_logo_header_page) 
* click_by_logo_and_switch_to_new_tab - скролл до выпадающего списка
* find_and_get_title_on_new_page - клик по элементу списка и получение текста ответа
* find_and_click_by_logo - Клик по лого
* find_and_get_element_on_new_page - элемент на новой странице


### Локаторы
#### faq_page_locators (локаторы для test_faq_page) 
#### order_page_locators (методы для test_order_page) 
#### logo_header_page_locators (методы для test_logo_header_page) 