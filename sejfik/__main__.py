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

        if show_logs:
            pass

        if disable_image_load:
            chrome_prefs['images': 2]

        if platform == 'linux' or platform == 'linux2':
            pass

        elif platform == 'darwin':
            pass

        elif platform == 'win32':
            pass

        def get_sejfik_logger(self, show_logs: bool):
            """Handles the creation of logger"""

        def find_chromedriver(self):
            """Finds chromedriver binaries"""

        def download_chromedriver(self):
            """Downloads chromedriver binaries"""

        def set_selenium_session(self, logger):
            """Starts selenium session"""
            
        def set_webui_session(self):
            """Starts web interface session on localhost"""

        def login(self):
            """Login the user either with the username and password"""
            
        def get_ptc_links(self):
            """Scrapes pay to click links"""
            
        def get_inbox_links(self):
            """Scrapes inbox links"""
            
        def get_startpage_link(self):
            """Scrapes and cache starting page link"""
            
