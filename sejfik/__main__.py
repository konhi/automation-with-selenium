import configparser
import logging
from sys import platform

import selenium

from sejfik import constants, downloader, utils


class Sejfik:
    """Class to be instantiated to use the script"""

    def __init__(
        self,
        username: str = None,
        password: str = None,
        page_delay: int = 25,
        show_logs: bool = True,
        save_logs: bool = None,
        logs_path: str = None,
        proxy_username: str = None,
        proxy_password: str = None,
        proxy_address: str = None,
        proxy_port: str = None,
        vpn_server: str = None,
        webui_interface: bool = False,
        disable_image_load: bool = True,
        chromedriver_headless: bool = True,
        chromedriver_path: str = None,
        chromedriver_arguments: list = None,
        chrome_prefs: dict = None,
    ):
        if self.chromedriver_headless:
            chromedriver_arguments.extend(
                ['--headless',
                 '--disable-gpu']
            )

        self.username = username
        self.password = password
        self.page_delay = page_delay

        if disable_image_load:
            chrome_prefs['images': 2]

        def set_logger(self, show_logs: bool):
            """Handles the creation of logger"""

            if show_logs:
                logging.basicConfig(
                    filename=logs_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
                
            logging.debug('Set up logger.')

            return self

        def find_chromedriver(self):
            """Finds chromedriver binaries"""

            return self

        def download_chromedriver(self):
            """Downloads chromedriver binaries"""

            return self

        def set_selenium_session(self, logger):
            """Sets selenium session"""

            if platform == 'linux' or platform == 'linux2':
                logging.debug('Linux has been detected.')

            elif platform == 'darwin':
                logging.debug('Mac OS has been detected.')

            elif platform == 'win32':
                logging.debug('Windows has been detected.')

            logging.debug('Selenium session has been started.')

            return self

        def set_webui_session(self):
            """Sets web interface session on localhost"""

            logging.debug('WebUI session has been started.')

            return self

        def login(self):
            """Login the user either with the username and password"""

            logging.debug('Logged in.')

            return self

        def get_ptc_links(self):
            """Scrapes pay to click links"""

            logging.debug('Scrapped pay to click links.')

            return self

        def get_inbox_links(self):
            """Scrapes inbox links"""

            logging.debug('Scrapped inbox links.')

            return self

        def get_startpage_link(self):
            """Scrapes and cache starting page link"""

            logging.debug('Scrapped start page link.')

            return self
