"""Frequently used data.

Data:
    driver_settings: settings of selenium chromedriver.

    prefs: preferences to set accepting languages, disable images and
    javascript for faster loading.

    urls: links to pages.

    xpaths: groupped xpaths to allow scrapping elements from the webpages.

    Typical usage examples:
    >>> self.driver.get(urls['login'])
"""
from typing import Any, Dict, Tuple

from selenium.webdriver.common.keys import Keys

driver_settings: Tuple[str, ...] = (
    '--profile-directory=Default',
    '--disable-plugins-discovery',
    '--start-maximized',
    '--log-level=3',
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537h.36',
)

prefs: Dict[str, Any] = {
    'profile.default_content_setting_values': {'images': 2},
    'intl.accept_languages': 'pl-PL',
    'profile.managed_default_content_settings.javascript': 2,
}

urls: Dict[str, str] = {
    'login': 'https://example.com/pages/enter.php',
    'ptc': 'https://example.com/pages/ptcontest.php?startpos=',
    'ptc_paid': 'https://example.com/pages/ptc.php?startpos=',
    'inbox': 'https://example.com/pages/inbox.php',
    'starting_page': 'https://example.com/pages/startowa.php',
    'ublock_settings': 'chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/1p-filters.html',
    'earnings': 'https://example.com/pages/earnings.php',
}

xpaths: Dict[str, Dict[str, str]] = {
    'login': {
        'username_input': 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="username"]',
        'password_input': 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="password"]',
        'login_button': 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="submit"]',
    },
    'enter': {
        "username": 'html/body/div[@class="green-box"]/div[@class="container-top"]\
            /div[@class="user"]/a[@href="https://example.com/pages/profil.php"]/span'
    },
    'ptc': {
        'anchor': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title" and not(center)]\
                /a[@target="_ptc" and not(img)]',
        'anchor_alt': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title"]/a[@target="_ptc" and img]',
    },
    'inbox': {
        'anchor': 'html/body/div[@class="container"]/div/div[@class="content-width referers"]\
            /div[@class="inbox_table"]/form/table/tbody/tr/td[2]/a',
    },
    'starting_page': {
        'user_starting_page': 'html/body/div[@class="container"]/div[@class="content"]/p/b',
    },
    'ublock_settings': {
        'save_button': '//*[@id="userFiltersApply"]',
    },
    'earnings': {
        'money': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="inbox_table"]/table/tbody/tr/td/b',
        'points': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="inbox_table"]/table/tbody/tr[4]/td[@class="wages_point"]',
    },
}

ANTICHEAT_WORDS = (
    'sprawdza',
    'uwaga',
    'weryfik',
    'zatwier',
    'potwier',
)

PARTIAL_INBOX_LINK = 'http://example.com/scripts/runner.php?EA'
UBLOCK_SEND_KEYS = '##iframe{0}*.css{0}*.ico'.format(Keys.ENTER)
