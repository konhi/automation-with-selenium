from typing import Dict, Tuple, Any, List

from selenium.webdriver.remote.webelement import WebElement  # type: ignore

driver_settings: List[str] = [
    '--profile-directory=Default',
    '--disable-plugins-discovery',
    '--start-maximized',
    '--log-level=3',
    '--start-incognito',
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537.36'
]

driver_settings_headless: Tuple[str, ...] = (
    '--headless',
    '--disable-gpu'
)

prefs: Dict[str, Any] = {
    'profile.default_content_setting_values': {
        'images': 2
    },
    'intl.accept_languages': 'pl-PL',
    'profile.managed_default_content_settings.javascript': 2,
}

urls: Dict[str, str] = {
    'login': 'https://sejfik.com/pages/enter.php',
    'ptc': 'https://sejfik.com/pages/ptcontest.php?startpos=',
    'ptc_paid': 'https://sejfik.com/pages/ptc.php?startpos=',
    'inbox': 'https://sejfik.com/pages/inbox.php',
    'starting_page': 'https://sejfik.com/pages/startowa.php'
}

xpaths: Dict[str, Dict[str, str]] = {
    'login': {
        'username_input': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table\
            /tbody/tr/td/input[@name="username"]',
        'password_input': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table\
            /tbody/tr/td/input[@name="password"]',
        'login_button': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table/tbody\
            /tr/td/input[@name="submit"]'
    },

    'enter': {
        'username': 'html/body/div[@class="green-box"]/div[@class="container-top"]/div[@class="user"]\
            /a[@href="https://sejfik.com/pages/profil.php"]/span'
    },

    'ptc': {
        'anchor': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title" and not(center)]/a[@target="_ptc" and not(img)]',
        'anchor_alt': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title"]/a[@target="_ptc" and img]',
    },

    'inbox': {
        'anchor': 'html/body/div[@class="container"]/div/div[@class="content-width referers"]/div[@class="inbox_table"]\
            /form/table/tbody/tr[2]/td[2]/a'
    },

    'starting_page': {
        'user_starting_page': 'html/body/div[@class="container"]/div[@class="content"]/p/b'
    }
}

anticheat_words = [
    'sprawdza',
    'uwaga',
    'weryfik',
    'zatwier',
    'potwier',
]


def get_href(element: WebElement) -> Any:
    """Returns href from WebElement or None if there's no href"""

    return element.get_attribute('href')


def verify_and_get_href(element: WebElement) -> Any:
    """Returns href from WebElement if it not contains anti-cheat words."""

    text = element.text

    for w in anticheat_words:
        if w in text:
            return

    return element.get_attribute('href')
