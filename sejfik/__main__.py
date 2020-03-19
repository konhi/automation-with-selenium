import logging
from typing import Iterator, List, Tuple, Dict

from selenium.webdriver.remote.webelement import WebElement  # type: ignore

from .browser import set_selenium_session  # type: ignore
from .utils import get_href, urls, xpaths, prefs  # type: ignore


class Sejfik:
    """Class to be instantiated to use the script."""

    def __init__(
        self,
        username: str,
        password: str,
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

    def get_ptc_links(self) -> Iterator[str]:
        """
        Scrapes pay to click links.

        :returns: iterator of links.
        """

        anchors: List[WebElement] = []
        isscrapped: bool = False

        while not isscrapped:
            i: int = 0

            self.driver.get(urls['ptc'] + str(i * 15))

            current_anchors: Tuple[List[WebElement], ...] = (
                self.driver.find_elements_by_xpath(
                    xpaths['ptc']['anchor_alt']),
                self.driver.find_elements_by_xpath(xpaths['ptc']['anchor'])
            )

            if not len(current_anchors[0]) and not len(current_anchors[1]):
                anchors.extend(current_anchors[0] + current_anchors[1])
                i += 1

            else:
                isscrapped = True

        logging.debug('Scrapped pay to click links.')

        return map(get_href, anchors)
