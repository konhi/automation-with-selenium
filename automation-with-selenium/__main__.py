"""Tool for automated tasks.

Uses Python 3.8 and mainly Selenium library to control Chrome browser.
Contains:

    login(): Logs in user to webpage.

    get_ptc_links(): Scrapes Pay To Click links.

    get_inbox_links(): Scrapes Inbox links.

    open_links(links): Open every link of the list.

    close_browser(timer): Closes browser after given time.

Typical usage example:

    >>> bot = automation-with-selenium('username', 'password')
    >>> ptc_links = bot.get_ptc_links()
"""

import logging
from typing import Any, List, NoReturn, Tuple

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from automation.browser import set_selenium_session
from automation import PARTIAL_INBOX_LINK, urls, xpaths
from automation import get_href, verify_and_get_href


class AutomationWithSeleniumBase(object):
    """Base class to be instantiated to use the script."""

    def __init__(
        self,
        *,
        show_logs: bool = True,
    ) -> None:
        """Initialize global arguments.

        Args:
            show_logs: shall script show logs.

        """
        self.driver = set_selenium_session()

        if show_logs:
            logging.basicConfig(
                format='[%(levelname)s | %(asctime)s] %(message)s',
                datefmt='%H:%M:%S',
                level=logging.INFO,
            )

    def __enter__(self):
        """Start driver on session open.

        Returns:
            self: automation-with-selenium object.
        """
        return self

    def __exit__(self, exception_type, exception_value, traceback) -> NoReturn:
        """Quit driver on session end.

        Arguments:
            exception_type: type of exception raised during session.
            exception_value: value of exception raised during session.
            traceback: traceback of exception raised durring session.
        """
        self.driver.quit()

    def login(self, username: str, password: str) -> None:
        """Log in user to page.

        Args:
            username: username or e-mail.
            password: password.

        """
        self.driver.get(urls['login'])
        logging.info('Loaded homepage.')

        self.driver.find_element_by_xpath(xpaths['login']['username_input']).send_keys(
            username,
        )

        self.driver.find_element_by_xpath(xpaths['login']['password_input']).send_keys(
            password,
        )

        self.driver.find_element_by_xpath(
            xpaths['login']['login_button'],
        ).click()

        logging.debug('Logged in.')


class AutomationWithSeleniumPTC(AutomationWithSeleniumBase):
    """Pay to Click class to be instantiated to use the script."""

    def __init__(
        self,
        *,
        links_per_page: int = 15,
    ) -> None:
        """Initialize global arguments, inherit from AutomationWithSeleniumBase __init__.

        Args:
            links_per_page: how many links per page.
        """
        super().__init__()
        self.links_per_page = links_per_page

    def get_ptc_links(self) -> List[str]:
        """Get pay to click links.

        Returns:
            List: raw hrefs (e.g. https://xxxxxxx.com/...)
        """
        page_index = 0
        links: List = []

        while True:
            url_to_visit = urls['ptc'] + str(page_index * self.links_per_page)
            self.driver.get(url_to_visit)
            logging.info('Loaded next pay to click page.')

            current_anchors: Tuple[List[WebElement], ...] = (
                self.driver.find_elements_by_xpath(
                    xpaths['ptc']['anchor_alt'],
                ),
                self.driver.find_elements_by_xpath(xpaths['ptc']['anchor']),
            )

            if not current_anchors[0] and not current_anchors[1]:
                break

            else:
                links += [verify_and_get_href(web_el)
                          for web_el in current_anchors[0] + current_anchors[1]]

                page_index += 1

        logging.info('Pay to click links has been scrapped.')

        return links

    def get_inbox_links(self) -> Any:
        """Scrape newest inbox links.

        Returns:
            Any:
                List: inbox links if mail is present.

                None: if mail not present.

        """
        self.driver.get(urls['inbox'])
        logging.info('Loaded inbox page.')

        try:
            mail_link = get_href(
                self.driver.find_element_by_xpath(xpaths['inbox']['anchor']),
            )
        except NoSuchElementException:
            logging.info('Mail not found.')

            return None

        self.driver.get(mail_link)
        logging.info('Loaded mail.')

        mail_links = self.driver.find_elements_by_partial_link_text(
            PARTIAL_INBOX_LINK,
        )

        return [get_href(link) for link in mail_links]

    def open_links(self, links: List[str]) -> None:
        """Open links.

        Args:
            links (Link[str]): list of links.

        """
        for link in links:
            self.driver.execute_script('window.open(arguments[0]);', link)
            logging.info('Oppened link.')

        logging.info('Oppened %s links.', len(links))
