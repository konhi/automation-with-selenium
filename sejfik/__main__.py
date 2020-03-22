"""Tool for automated sejfik tasks.

Uses Python 3.8 and mainly Selenium library to control Chrome browser.
Contains:

    login(): Logs in user to sejfik webpage.

    get_ptc_links(): Scrapes Pay To Click links.

    get_inbox_links(): Scrapes Inbox links.

    open_links(links): Open every link of the list.

    close_browser(timer): Closes browser after given time.

Typical usage example:

    >>> bot = Sejfik('username', 'password', chromedriver_headless=True)
    >>> ptc_links = bot.get_ptc_links()
"""


import logging
from collections import deque
from time import sleep
from typing import Deque, List, Tuple, Any

from selenium.webdriver.remote.webelement import WebElement  # type: ignore
from selenium.common.exceptions import NoSuchElementException  # type: ignore

from .browser import set_selenium_session  # type: ignore
from .utils import get_href, urls, verify_and_get_href, xpaths  # type: ignore


class Sejfik:
    """Class to be instantiated to use the script."""

    def __init__(
        self,
        username: str,
        password: str,
        *,
        timer: int = 35,
        show_logs: bool = True,
        #  save_logs: bool = False,
        logs_path: str = "",
        chromedriver_headless: bool = False
    ) -> None:

        self.username = username
        self.password = password
        self.timer = timer
        self.show_logs = show_logs
        self.logs_path = logs_path
        self.driver = set_selenium_session(
            chromedriver_headless=chromedriver_headless)

        if show_logs:
            logging.basicConfig(
                filename=self.logs_path,
                filemode="a",
                format="[%(levelname)s | %(asctime)s] %(message)s",
                datefmt="%H:%M:%S",
                level=logging.INFO,
            )

        print(":'######::'########:::::::'##:'########:'####:'##:::'##:")
        print(":''##... ##: ##.....:::::::: ##: ##.....::. ##:: ##::'##::")
        print(" ##:::..:: ##::::::::::::: ##: ##:::::::: ##:: ##:'##:::")
        print(". ######:: ######::::::::: ##: ######:::: ##:: #####::::")
        print(":..... ##: ##...::::'##::: ##: ##...::::: ##:: ##. ##:::")
        print("'##::: ##: ##::::::: ##::: ##: ##:::::::: ##:: ##:. ##::")
        print(". ######:: ########:. ######:: ##:::::::'####: ##::. ##:")
        print(":......:::........:::......:::..::::::::....::..::::..::")
        print("")
        print("Sejfik-Bot | functions:")
        print("- login")
        print("- get_ptc_links")
        print("- get_inbox_links")
        print("- open_links")
        print("")
        print("Starting app. Hello {}!".format(self.username))

    def login(self) -> None:
        """Login the user either with the username and password."""

        self.driver.get(urls["login"])
        logging.info("Loaded login page.")

        self.driver.find_element_by_xpath(xpaths["login"]["username_input"]).send_keys(
            self.username
        )

        self.driver.find_element_by_xpath(xpaths["login"]["password_input"]).send_keys(
            self.password
        )

        self.driver.find_element_by_xpath(
            xpaths["login"]["login_button"]).click()

        logging.debug("Logged in.")

    def get_ptc_links(self) -> Deque[str]:
        """Get pay to click links.

        Returns:

            Deque: raw hrefs
        """

        isscrapped = False
        i = 0
        links: Deque[str] = deque()

        while not isscrapped:
            self.driver.get(urls["ptc"] + str(i * 15))
            logging.info("Loaded next pay to click page.")

            current_anchors: Tuple[List[WebElement], ...] = (
                self.driver.find_elements_by_xpath(
                    xpaths["ptc"]["anchor_alt"]),
                self.driver.find_elements_by_xpath(xpaths["ptc"]["anchor"]),
            )

            if not current_anchors[0] and not current_anchors[1] == 0:
                isscrapped = True

            else:
                for web_el in current_anchors[0] + current_anchors[1]:
                    if web_el:
                        links.append(verify_and_get_href(web_el))

                i += 1

        logging.info("Pay to click links has been scrapped.")

        return links

    def get_inbox_links(self) -> Any:
        """Scrapes newest inbox links.

        Returns:

            Deque: inbox links if mail is present.

            None: if mail not present.
        """

        self.driver.get(urls["inbox"])
        logging.info("Loaded inbox page.")

        try:
            mail_link = get_href(
                self.driver.find_element_by_xpath(xpaths["inbox"]["anchor"])
            )

            self.driver.get(mail_link)
            logging.info("Loaded mail.")

            logging.info("Scrapped mail links.")

            return deque(
                [
                    get_href(x)
                    for x in self.driver.find_elements_by_partial_link_text(
                        "http://sejfik.com/scripts/runner.php?EA="
                    )
                ]
            )

        except NoSuchElementException:
            logging.debug('Mail not found.')

            return None

    def open_links(self, links: Deque[str]) -> None:
        """Open links.

        Args:

            links (Deque): list of links.
        """

        for link in links:
            self.driver.execute_script("window.open(arguments[0]);", link)
            logging.info("Oppened link.")

        logging.info("Oppened %s links. That's a lot!", len(links))

    def close_browser(self, timer: int = 60) -> None:
        """Closes browser.

        Args:

            timer (int): time to wait before closing browser.
        """

        sleep(timer)
        logging.info("Closing browser after %s seconds", timer)
        self.driver.quit()
        logging.info("Closed browser.")
