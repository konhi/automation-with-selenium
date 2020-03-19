from os.path import dirname, realpath
from platform import system
from shutil import Error, move
from typing import List

from selenium import webdriver  # type: ignore
from webdriverdownloader import ChromeDriverDownloader  # type: ignore

from .utils import driver_settings, driver_settings_headless, prefs  # type: ignore


def get_chromedriver() -> str:
    """Downloads chromedriver binary if not present, moves to /bin folder.

    :returns: path to chromedriver binary."""

    current_path = dirname(realpath(__file__))
    binaries_path = '{}/../bin/'.format(current_path)

    cdd = ChromeDriverDownloader()
    sym_path: str = cdd.download_and_install()[1]

    try:
        move(sym_path, '{}/../bin'.format(current_path))

    except Error:
        pass

    if system() == 'Windows':
        return '{}/chromedriver.exe'.format(binaries_path)

    else:
        return '{}/chromedriver'.format(binaries_path)


def set_selenium_session(
        proxy_address: str = '',
        chromedriver_headless: bool = False,
        chromedriver_arguments: List[str] = driver_settings) -> webdriver:
    """Starts selenium session."""

    if chromedriver_headless:
        chromedriver_arguments.extend(driver_settings_headless)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)

    for arg in chromedriver_arguments:
        chrome_options.add_argument(arg)

    driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    return driver
