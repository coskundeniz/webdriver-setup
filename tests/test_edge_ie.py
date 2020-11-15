import os
import sys
import unittest

from selenium import webdriver
from selenium.webdriver import ChromeOptions, IeOptions

from webdriver_setup.get_webdriver import get_webdriver_for

# turn off WDM logs
os.environ["WDM_LOG_LEVEL"] = "0"


@unittest.skipUnless(sys.platform.startswith("win"), "Test requires Windows")
class TestEdgeDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_edge_driver(self):

        self.driver = get_webdriver_for("edge")
        self.assertIsInstance(self.driver, webdriver.Edge)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("EDge")
        self.assertIsInstance(self.driver, webdriver.Edge)

    def test_passing_options(self):

        edge_options = ChromeOptions()
        edge_options.add_argument("--headless")

        self.driver = get_webdriver_for("edge", options=edge_options)
        self.assertIsNotNone(self.driver)
        self.assertTrue(edge_options.headless)


@unittest.skipUnless(sys.platform.startswith("win"), "Test requires Windows")
class TestIeDriver(unittest.TestCase):

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_get_ie_driver(self):

        self.driver = get_webdriver_for("ie")
        self.assertIsInstance(self.driver, webdriver.Ie)

    def test_with_mixed_case_browser_name(self):

        self.driver = get_webdriver_for("Ie")
        self.assertIsInstance(self.driver, webdriver.Ie)

    def test_passing_options(self):

        ie_options = IeOptions()
        ie_options.ensure_clean_session = True
        ie_options.ignore_protected_mode_settings = True

        self.driver = get_webdriver_for("ie", options=ie_options)
        self.assertIsNotNone(self.driver)
        self.assertTrue(ie_options.ensure_clean_session)
        self.assertTrue(ie_options.ignore_protected_mode_settings)


if __name__ == "__main__":
    unittest.main()
