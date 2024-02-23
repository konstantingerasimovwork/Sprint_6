import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    service = Service(
        executable_path='/Users/macbook/Desktop/WebDriver/bin/geckodriver')
    browser = webdriver.Firefox(service=service, options=options)
    # browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    yield browser
    browser.quit()
