"""Contains functions needed to start webdriver.

Contains:

    get_chromedriver(): Making sure there will be chromedriver binary to run.
    _set_selenium_session(): Starts selenium session.

Typical usage example:

    >>> driver = _set_selenium_session(chromedriver_headless=True)
"""

from os.path import dirname, realpath
from platform import system
# from shutil import Error, move
from time import sleep

from selenium import webdriver
# from webdriverdownloader import ChromeDriverDownloader

from automation.data import UBLOCK_SEND_KEYS, driver_settings, prefs, urls, xpaths


def _get_chromedriver() -> str:
    """Download chromedriver binary and moves to /bin folder if not present.

    Returns:
        str: path to chromedriver binary file.
    """
    """
    WebDriverDownloader isn't working lately, need fix.

        current_path = dirname(realpath(__file__))
        binaries_path = '{0}/../bin/'.format(current_path)

        cdd = ChromeDriverDownloader()
        sym_path: str = cdd.download_and_install()[1]

        try:
            move(sym_path, '{0}/../bin'.format(current_path))

        except Error:
            pass
    """
    current_path = dirname(realpath(__file__))
    binaries_path = '{0}/../bin/'.format(current_path)

    if system() == 'Windows':
        return '{0}/chromedriver.exe'.format(binaries_path)

    return '{0}/chromedriver'.format(binaries_path)


def set_selenium_session() -> webdriver:
    """Start selenium session with proper options and extension settings.

    Returns:
        webdriver: driver object.
    """
    current_path = dirname(realpath(__file__))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_extension(
        '{0}/../bin/extension_1_24_4_0.crx'.format(current_path))

    for arg in driver_settings:
        chrome_options.add_argument(arg)

    driver = webdriver.Chrome(_get_chromedriver(), options=chrome_options)

    driver.get(urls['ublock_settings'])

    # Using sleep to fix some javascript input's issues.

    input_line = driver.switch_to.active_element
    sleep(2)

    input_line.send_keys(UBLOCK_SEND_KEYS)
    sleep(2)

    driver.find_element_by_xpath(
        xpaths['ublock_settings']['save_button']).click()

    return driver
