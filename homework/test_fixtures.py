"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture
def desktop_browser():
    browser.config.window_width = 1440
    browser.config.window_height = 900


@pytest.fixture
def mobile_browser():
    browser.config.window_width = 375
    browser.config.window_height = 740


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

