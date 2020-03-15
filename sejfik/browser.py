from os.path import dirname, realpath
from shutil import move

from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader

from sejfik import utils


def get_chromedriver() -> None:
    """
    Downloads chromedriver binaries if not present, moves to /bin folder.
    """

    cdd = ChromeDriverDownloader()        
    sym_path: str = cdd.download_and_install()[1]

    move(sym_path, '{}/../bin'.format(dirname(realpath(__file__))))


def set_selenium_session(
        proxy_address,
        proxy_port,
        proxy_username,
        proxy_password,
        vpn_server,
        page_delay: int = 25,
        chromedriver_headless: bool = True,
        chromedriver_arguments: list = []) -> webdriver:
    """
    Starts session for a selenium server.

    :returns: WebDriver as driver object.
    """

    chromedriver_arguments.extend(utils.driver_settings)

    if chromedriver_headless:
        chromedriver_arguments.extend(utils.driver_settings_headless)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', utils.prefs)

    for arg in chromedriver_arguments:
        chrome_options.add_argument(arg)

    driver = webdriver.Chrome(get_chromedriver(), options=chrome_options)

    return driver
