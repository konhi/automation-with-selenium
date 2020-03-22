"""Contains functions needed to start webdriver.

Contains:

    get_chromedriver(): Making sure there will be chromedriver binary to run.
    set_selenium_session(): Starts selenium session.

Typical usage example:

    >>> driver = set_selenium_session(chromedriver_headless=True)
"""

from os.path import dirname, realpath
from platform import system
from shutil import Error, move
from time import sleep

from selenium import webdriver  # type: ignore
from webdriverdownloader import ChromeDriverDownloader  # type: ignore

from .utils import driver_settings, driver_settings_headless, prefs, urls, xpaths  # type: ignore


def get_chromedriver() -> str:
    """Downloads chromedriver binary and moves to /bin folder if not present.

    Returns:

        str: path to chromedriver binary file.
    """

    current_path = dirname(realpath(__file__))
    binaries_path = "{}/../bin/".format(current_path)

    cdd = ChromeDriverDownloader()
    sym_path: str = cdd.download_and_install()[1]

    try:
        move(sym_path, "{}/../bin".format(current_path))

    except Error:
        pass

    if system() == "Windows":
        return "{}/chromedriver.exe".format(binaries_path)

    return "{}/chromedriver".format(binaries_path)


def set_selenium_session(chromedriver_headless: bool = False) -> webdriver:
    """Starts selenium session with proper options and extension settings.

    Returns:

        WebDriver: driver object.
    """

    current_path = dirname(realpath(__file__))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_extension(
        current_path + '/../bin/extension_1_24_4_0.crx')

    for arg in driver_settings:
        chrome_options.add_argument(arg)

    if chromedriver_headless:
        for arg in driver_settings_headless:
            chrome_options.add_argument(arg)

        driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    else:
        driver.get(urls['ublock_settings'])

        # Using sleep to fix some javascript input's issues.

        input_line = driver.switch_to.active_element
        sleep(2)

        input_line.send_keys('##iframe')
        sleep(2)

        driver.find_element_by_xpath(xpaths['ublock_settings']['save_button']).click()

        driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    return driver
