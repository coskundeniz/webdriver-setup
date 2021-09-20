from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_setup.driver import DriverBase


class ChromeDriver(DriverBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def create_driver(self, **kwargs):
        """Create Chrome webdriver

        :type kwargs: dict
        :param kwargs: Optional arguments
        :rtype: selenium.webdriver.Chrome
        :returns: Chrome webdriver instance
        """

        cache_timeout = kwargs.get("cache_valid_range", 7)

        driver_path = ChromeDriverManager(cache_valid_range=cache_timeout).install()

        try:
            return webdriver.Chrome(driver_path, **kwargs)
        except:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            return webdriver.Chrome(driver_path, options=options, **kwargs)
