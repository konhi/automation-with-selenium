"""Frequently used functions.

Functions:
    verify_and_get_href: return href attribute after verification.

Typical usage examples:
    >>> links.append(verify_and_get_href(web_el))
"""
from typing import Any

from selenium.webdriver.remote.webelement import WebElement


def verify_and_get_href(element: WebElement) -> Any:
    """Verify and get href attribute.

    Args:
        element: WebElement from Selenium WebDriver.

    Returns:
        Any: href (str) or None if no href attribute or contains anti-cheat
        word.
    """
    anticheat_words = (
        'sprawdza',
        'uwaga',
        'weryfik',
        'zatwier',
        'potwier',
    )

    title = element.text

    for word in anticheat_words:
        if word in title:
            return None

    return element.get_attribute('href')


def get_href(element: WebElement) -> Any:
    """Verify and get href attribute.

    Args:
        element: WebElement from Selenium WebDriver.

    Returns:
        Any: href (str) or None if no href attribute.
    """
    return element.get_attribute('href')
