import pytest
from selene.support.shared import browser
from selene import be, have
from selenium.webdriver.chrome import webdriver


@pytest.fixture
def browser_size():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    driver.set_window_size(1920, 1080)
    yield
    browser.quit()


def test_first(browser_size):
    browser.open('https://google.com')
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_second(browser_size):
    browser.open('https://google.com')
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('jjjjjjjjkknjknkjknkjj,k').press_enter()
    browser.element('[id="search"]').should(
    have.text('Podana fraza - jjjjjjjjkknjknkjknkjj,k - nie została odnaleziona.'))