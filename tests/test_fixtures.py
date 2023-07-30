from selene import be, have
from selene.support.shared import browser


def test_first():
    browser.open('https://google.com')
    browser.element('#L2AGLb').click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented '))


def test_second():
    browser.open('https://google.com')
    browser.element('#L2AGLb').click()
    browser.element('[name="q"]').should(be.blank).type('jjjjjjjjkknjknkjknkjj,k').press_enter()
    browser.element('#topstuff').should(
        have.text('Podana fraza - jjjjjjjjkknjknkjknkjj,k'))
