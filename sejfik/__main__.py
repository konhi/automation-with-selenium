import logging
import os
from collections import deque

import selenium
from selenium.webdriver.remote.webelement import WebElement

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
        self.proxy_adress = proxy_address

        self.driver = set_selenium_session()

    def set_logger(self, show_logs: bool):
        """Handles the creation of logger."""

        if show_logs:
            logging.basicConfig(
                filename=self.logs_path,
                filemode='a',
                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                datefmt='%H:%M:%S',
                level=logging.DEBUG)

        logging.debug('Set up logger.')

    def login(self) -> None:
        """Login the user either with the username and password."""

        self.driver.get(urls['login'])

        self.driver.find_element_by_xpath(
            xpaths['login']['username_input']).send_keys(self.username)

        self.driver.find_element_by_xpath(
            xpaths['login']['password_input']).send_keys(self.password)

        self.driver.find_element_by_xpath(
            xpaths['login']['login_button']).click()

        logging.debug('Logged in.')

    def get_ptc_links(self) -> map:
        """
        Scrapes pay to click links.

        :returns: iterator of full links.
        """

        def get_href(x: WebElement) -> str:
            return x.get_attribute('href')

        self.driver.get(urls['ptc'])

        logging.debug('Scrapped pay to click links.')

        anchors = self.driver.find_elements_by_xpath(
            xpaths['ptc']['anchor_alt']) + self.driver.find_elements_by_xpath(
            xpaths['ptc']['anchor'])

        return map(get_href, anchors)

    def get_inbox_links(self):
        """Scrapes inbox links."""

        logging.debug('Scrapped inbox links.')

    def get_startpage_link(self):
        """Scrapes and cache starting page link."""

        logging.debug('Scrapped start page link.')
