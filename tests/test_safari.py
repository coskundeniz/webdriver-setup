import os
import sys
import unittest

from selenium import webdriver

from webdriver_setup.get_webdriver import get_webdriver_for

# turn off WDM logs
os.environ["WDM_LOG_LEVEL"] = "0"


@unittest.skipUnless(sys.platform.startswith("darwin"), "Test requires Mac OS")
class TestSafariDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_safari_driver(self):

        self.driver = get_webdriver_for("safari")
        self.assertIsInstance(self.driver, webdriver.Safari)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("SafaRI")
        self.assertIsInstance(self.driver, webdriver.Safari)


if __name__ == "__main__":
    unittest.main()
