import os

from selenium import webdriver
import selenium
from webdriverdownloader import ChromeDriverDownloader

from sejfik import utils


def get_chromedriver():
    """
    Downloads chromedriver binaries if not present.
    
    :returns: Sym path to chromedriver binary or None.
    """

    chromedriver_path: str = '{}/../bin/chromedriver'.format(
        os.path.dirname(os.path.abspath(__file__)))

    if os.path.isfile(chromedriver_path) or os.path.isfile(chromedriver_path + '.exe'):
        logging.debug('Chromedriver exists.')
        
        return None

    else:
        logging.debug("Chromedriver don't exists.")
        sym_path: str = ChromeDriverDownloader.download_and_install()[1]
        
        return sym_path


def set_selenium_session(
        proxy_address,
        proxy_port,
        proxy_username,
        proxy_password,
        vpn_server,
        page_delay: int = 25,
        chromedriver_headless: bool = True,
        chromedriver_arguments: list = None) -> WebDriver:
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