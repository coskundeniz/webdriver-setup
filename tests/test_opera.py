import os
import unittest

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from webdriver_setup.get_webdriver import get_webdriver_for

# turn off WDM logs
os.environ["WDM_LOG_LEVEL"] = "0"


class TestOperaDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_opera_driver(self):

        self.driver = get_webdriver_for("opera")
        self.assertIsInstance(self.driver, webdriver.Opera)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("OperA")
        self.assertIsInstance(self.driver, webdriver.Opera)

    def test_passing_options(self):

        opera_options = ChromeOptions()
        opera_options.add_argument("start-maximized")

        self.driver = get_webdriver_for("opera", options=opera_options)
        self.assertIsNotNone(self.driver)
        self.assertIn("start-maximized", opera_options.capabilities["goog:chromeOptions"]["args"])


if __name__ == "__main__":
    unittest.main()
