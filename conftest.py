import pytest
from selene import browser


@pytest.fixture(autouse=True)
def config_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
