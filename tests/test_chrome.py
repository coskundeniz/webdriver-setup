import os
import unittest

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from webdriver_setup.get_webdriver import get_webdriver_for

# turn off WDM logs
os.environ["WDM_LOG_LEVEL"] = "0"


class TestChromeDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_chrome_driver(self):

        self.driver = get_webdriver_for("chrome")
        self.assertIsInstance(self.driver, webdriver.Chrome)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("CHrOMe")
        self.assertIsInstance(self.driver, webdriver.Chrome)

    def test_passing_chrome_options(self):

        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("disable-gpu")

        self.driver = get_webdriver_for("chrome", options=chrome_options)
        self.assertIsNotNone(self.driver)
        self.assertTrue(chrome_options.headless)

    def test_invalid_browser_name(self):

        self.driver = None

        with self.assertRaises(ValueError):
            self.driver = get_webdriver_for("invalid_name")


if __name__ == "__main__":
    unittest.main()
