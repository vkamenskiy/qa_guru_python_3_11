"""
Переопределите параметр с помощью indirect
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


@pytest.mark.parametrize('browser_config', ['desktop_browser'], indirect=True)
def test_github_desktop(browser_config):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_config', ['mobile_browser'], indirect=True)
def test_github_mobile(browser_config):
    browser.open('https://github.com/')
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

