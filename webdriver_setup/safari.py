from selenium import webdriver
from webdriver_setup.driver import DriverBase


class SafariDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Safari webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Safari
        :returns: Safari webdriver instance
        """

        print("Run 'safaridriver --enable' from terminal if you didn't")

        return webdriver.Safari(**kwargs)
