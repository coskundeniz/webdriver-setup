from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager

from webdriver_setup.driver import DriverBase


class EdgeDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Edge webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Edge
        :returns: Edge webdriver instance
        """

        cache_timeout = kwargs.get("cache_valid_range", 7)

        driver_path = EdgeChromiumDriverManager(cache_valid_range=cache_timeout).install()

        return webdriver.Edge(driver_path, **kwargs)


class IeDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Internet Explorer webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Ie
        :returns: Ie webdriver instance
        """

        cache_timeout = kwargs.get("cache_valid_range", 7)

        driver_path = IEDriverManager(cache_valid_range=cache_timeout).install()

        return webdriver.Ie(driver_path, **kwargs)
