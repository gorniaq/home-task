from config.logger_config import logger
from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils


class NotificationHandler:

    @staticmethod
    def _wait_for_notification_to_disappear(driver, timeout=20):
        """
        Wait for the notification to disappear from the page.
        """
        # Wait until the notification is no longer visible on the page
        BrowserUtils.wait_for_element_invisibility(driver, BooksPageLocators.NOTIFICATION, timeout)
        logger.info("Notification has disappeared.")

    @staticmethod
    def _close_notification(driver, timeout=20):
        """
        Close the notification if it is present.
        """
        # Wait until the notification close button is clickable
        BrowserUtils.wait_for_element_and_click(driver, BooksPageLocators.NOTIFICATION_CLOSE_BTN, timeout)
        logger.info("Notification was closed.")

    @staticmethod
    def handle_notification(driver):
        """
        Handle the notification: close it if present, or wait for it to disappear.
        """
        # Attempt to close the notification
        NotificationHandler._close_notification(driver)
        # Wait for the notification to disappear if it was not closed
        NotificationHandler._wait_for_notification_to_disappear(driver)
