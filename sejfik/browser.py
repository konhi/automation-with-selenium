"""Contains functions needed to start webdriver.

Contains:

    get_chromedriver(): Making sure there will be chromedriver binary to run.
    set_selenium_session(): Starts selenium session.

Typical usage example:

    driver = set_selenium_session(chromedriver_headless=True)
"""

from os.path import dirname, realpath
from platform import system
from shutil import Error, move

from selenium import webdriver  # type: ignore
from webdriverdownloader import ChromeDriverDownloader  # type: ignore

from .utils import driver_settings, driver_settings_headless, prefs  # type: ignore


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
    """Starts selenium session with proper options.

    Returns:

        WebDriver: driver object.
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)

    for arg in driver_settings:
        chrome_options.add_argument(arg)

    if chromedriver_headless:
        for arg in driver_settings_headless:
            chrome_options.add_argument(arg)

    driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    return driver
