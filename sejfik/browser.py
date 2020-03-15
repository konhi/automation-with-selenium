from os.path import dirname, realpath
from shutil import move, Error
from platform import system

from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader

from sejfik import utils


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

    if system == 'win32':
        return '{}/chromedriver.exe'.format(binaries_path)

    else:
        return '{}/chromedriver'.format(binaries_path)


def set_selenium_session(
        proxy_address: str = None,
        proxy_port: str = None,
        proxy_username: str = None,
        proxy_password: str = None,
        vpn_server: str = None,
        page_delay: int = 25,
        chromedriver_headless: bool = False,
        chromedriver_arguments: list = []) -> webdriver:
    """Starts selenium session."""

    chromedriver_arguments.extend(utils.driver_settings)

    if chromedriver_headless:
        chromedriver_arguments.extend(utils.driver_settings_headless)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', utils.prefs)

    for arg in chromedriver_arguments:
        chrome_options.add_argument(arg)

    driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    return driver
