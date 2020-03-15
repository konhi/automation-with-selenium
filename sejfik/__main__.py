import logging
import os

import selenium

from .browser import get_chromedriver, set_selenium_session
from .utils import (anticheat_word, driver_settings, driver_settings_headless,
                    prefs, urls, xpaths)


class Sejfik:
    """Class to be instantiated to use the script."""

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
        chromedriver_headless: bool = False,
        chromedriver_arguments: list = None,
        chrome_prefs: dict = None,
    ):

        self.username = username
        self.password = password
        self.page_delay = page_delay

        self.driver = set_selenium_session(
            proxy_address, proxy_port, proxy_username, proxy_password, vpn_server)

    def set_logger(self, show_logs: bool):
        """Handles the creation of logger."""

        if show_logs:
            logging.basicConfig(
                filename=logs_path,
                filemode='a',
                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                datefmt='%H:%M:%S',
                level=logging.DEBUG)

        logging.debug('Set up logger.')

        return self

    def login(self):
        """Login the user either with the username and password."""
        driver.get(urls['login'])

        logging.debug('Logged in.')

        return self

    def get_ptc_links(self):
        """Scrapes pay to click links."""

        logging.debug('Scrapped pay to click links.')

        return self

    def get_inbox_links(self):
        """Scrapes inbox links."""

        logging.debug('Scrapped inbox links.')

        return self

    def get_startpage_link(self):
        """Scrapes and cache starting page link."""

        logging.debug('Scrapped start page link.')

        return self
