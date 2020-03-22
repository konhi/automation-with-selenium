"""Contains often used things.

Contains:
    driver_settings: settings of selenium chromedriver.

    driver_settings_headless: settings of selenium headless chromedriver.

    prefs: preferences to set accepting languages, disable images and javascript for faster loading.

    urls: links to pages.

    xpaths: groupped xpaths to allow scrapping elements from the webpages.

    ANTICHEAT_WORDS: list containing words to bypass verification.

    get_href: gets href attribute from element.

    verify_and_get_href: verify if doesn't contain words from ANTICHEAT_WORDS and gets href
    attribute from element.

    Typical usage examples:
    >>> self.driver.get(urls['login'])
"""


from typing import Any, Dict, Tuple

from selenium.webdriver.remote.webelement import WebElement  # type: ignore

driver_settings: Tuple[str, ...] = (
    "--profile-directory=Default",
    "--disable-plugins-discovery",
    "--start-maximized",
    "--log-level=3",
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537.36",
)

driver_settings_headless: Tuple[str, ...] = ("--headless", "--disable-gpu")

prefs: Dict[str, Any] = {
    "profile.default_content_setting_values": {"images": 2},
    "intl.accept_languages": "pl-PL",
    "profile.managed_default_content_settings.javascript": 2,
}

urls: Dict[str, str] = {
    "login": "https://sejfik.com/pages/enter.php",
    "ptc": "https://sejfik.com/pages/ptcontest.php?startpos=",
    "ptc_paid": "https://sejfik.com/pages/ptc.php?startpos=",
    "inbox": "https://sejfik.com/pages/inbox.php",
    "starting_page": "https://sejfik.com/pages/startowa.php",
    "ublock_settings": "chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/1p-filters.html",
}

xpaths: Dict[str, Dict[str, str]] = {
    "login": {
        "username_input": 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="username"]',
        "password_input": 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="password"]',
        "login_button": 'html/body/div[@class="container"]/div[@class="content"]\
            /form[@class="form-login"]/table/tbody/tr/td/input[@name="submit"]',
    },
    "enter": {
        "username": 'html/body/div[@class="green-box"]/div[@class="container-top"]\
            /div[@class="user"]/a[@href="https://sejfik.com/pages/profil.php"]/span'
    },
    "ptc": {
        "anchor": 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title" and not(center)]\
                /a[@target="_ptc" and not(img)]',
        "anchor_alt": 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]\
            /div[@class="box-content-row"]/div[@class="title"]/a[@target="_ptc" and img]',
    },
    "inbox": {
        "anchor": 'html/body/div[@class="container"]/div/div[@class="content-width referers"]\
            /div[@class="inbox_table"]/form/table/tbody/tr[2]/td[2]/a'
    },
    "starting_page": {
        "user_starting_page": 'html/body/div[@class="container"]/div[@class="content"]/p/b'
    },
    "ublock_settings": {
        "save_button": '//*[@id="userFiltersApply"]'
    },
}

ANTICHEAT_WORDS = [
    "sprawdza",
    "uwaga",
    "weryfik",
    "zatwier",
    "potwier",
]


def get_href(element: WebElement) -> Any:
    """Gets href attribute.

    Args:
        element (WebElement)

    Returns:
        Any: href (str) or None if no href attribute.
    """

    return element.get_attribute("href")


def verify_and_get_href(element: WebElement) -> Any:
    """Verifies and gets href attribute.

    Args:
        element (WebElement)

    Returns:
        Any: href (str) or None if no href attribute or contains anti-cheat word.
    """

    title = element.text

    for word in ANTICHEAT_WORDS:
        if word in title:
            return None

    return element.get_attribute("href")
