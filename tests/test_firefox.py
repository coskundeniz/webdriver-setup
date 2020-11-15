import os
import unittest

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from webdriver_setup.get_webdriver import get_webdriver_for

# turn off WDM logs
os.environ["WDM_LOG_LEVEL"] = "0"


class TestFirefoxDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_firefox_driver(self):

        self.driver = get_webdriver_for("firefox")
        self.assertIsInstance(self.driver, webdriver.Firefox)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("FireFoX")
        self.assertIsInstance(self.driver, webdriver.Firefox)

    def test_passing_firefox_options(self):

        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")

        self.driver = get_webdriver_for("firefox", options=firefox_options)
        self.assertTrue(self.driver.capabilities["moz:headless"])


if __name__ == "__main__":
    unittest.main()
