import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.window_height = 600
    browser.config.window_height = 1200
    yield

    browser.quit()
