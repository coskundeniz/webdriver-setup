from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from webdriver_setup.driver import DriverBase


class FirefoxDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Firefox webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Firefox
        :returns: Firefox webdriver instance
        """

        cache_timeout = kwargs.get("cache_valid_range", 7)

        driver_path = GeckoDriverManager(cache_valid_range=cache_timeout).install()

        return webdriver.Firefox(executable_path=driver_path, **kwargs)
