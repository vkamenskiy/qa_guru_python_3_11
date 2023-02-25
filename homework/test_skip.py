"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(
    params=[
        'mobile_browser',
        'desktop_browser'
    ],
    scope='session')
def browser_config(request):
    if request.param == 'mobile_browser':
        browser.config.window_height = 375
        browser.config.window_width = 650
    else:
        browser.config.window_height = 900
        browser.config.window_width = 1440


def test_github_desktop(browser_config):
    if browser.config.window_width < 1012:
        pytest.skip('Разрешение экрана мобильное')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_config):
    if browser.config.window_width > 1011:
        pytest.skip('Разрешение экрана десктопное')
    browser.open('https://github.com/')
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
