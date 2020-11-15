from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager

from webdriver_setup.driver import DriverBase


class OperaDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Opera webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Opera
        :returns: Opera webdriver instance
        """

        cache_timeout = kwargs.get("cache_valid_range", 7)

        driver_path = OperaDriverManager(cache_valid_range=cache_timeout).install()

        return webdriver.Opera(executable_path=driver_path, **kwargs)
