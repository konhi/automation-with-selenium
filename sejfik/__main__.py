import logging
from collections import deque
from typing import Deque, Dict, List, Tuple

from selenium.webdriver.remote.webelement import WebElement  # type: ignore

from .browser import set_selenium_session  # type: ignore
from .utils import prefs, urls, get_href, verify_and_get_href, xpaths  # type: ignore


class Sejfik:
    """Class to be instantiated to use the script."""

    def __init__(
        self,
        username: str,
        password: str,
        *,
        page_delay: int = 25,
        show_logs: bool = True,
        save_logs: bool = False,
        logs_path: str = '',
        proxy_username: str = '',
        proxy_password: str = '',
        proxy_address: str = '',
        proxy_port: str = '',
        vpn_server: str = '',
        chromedriver_headless: bool = False,
        chromedriver_arguments: List[str] = [],
        chrome_prefs: Dict[str, Dict[str, int]] = prefs,
    ) -> None:

        self.username = username
        self.password = password
        self.page_delay = page_delay
        self.show_logs = show_logs
        self.logs_path = logs_path
        self.proxy_adress = proxy_address
        self.logs_path = logs_path
        self.driver = set_selenium_session()

    def set_logger(self, show_logs: bool) -> None:
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

    def get_ptc_links(self) -> Deque[str]:
        """
        Scrapes pay to click links.

        :returns: Deque of links.
        """

        isscrapped = False
        i = 0
        links: Deque[str] = deque()

        while not isscrapped:
            self.driver.get(urls['ptc'] + str(i * 15))

            current_anchors: Tuple[List[WebElement], ...] = (
                self.driver.find_elements_by_xpath(
                    xpaths['ptc']['anchor_alt']),
                self.driver.find_elements_by_xpath(xpaths['ptc']['anchor'])
            )

            if len(current_anchors[0]) == 0 and len(current_anchors[1]) == 0:
                isscrapped = True

            else:
                for el in current_anchors[0] + current_anchors[1]:
                    links.append(verify_and_get_href(el))

                i += 1

        return links

    def get_inbox_links(self) -> Deque[str]:
        """
        Scrapes newest inbox links.

        :returns: Deque of links.
        """

        self.driver.get(urls['inbox'])

        mail_link = get_href(
            self.driver.find_element_by_xpath(xpaths['inbox']['anchor']))

        self.driver.get(mail_link)

        return deque([get_href(x) for x in self.driver.find_elements_by_partial_link_text(
            'http://sejfik.com/scripts/runner.php?EA=')])
