from webdriver_setup.firefox import FirefoxDriver
from webdriver_setup.chrome import ChromeDriver
from webdriver_setup.opera import OperaDriver
from webdriver_setup.safari import SafariDriver
from webdriver_setup.windows import EdgeDriver, IeDriver


def get_webdriver_for(browser, **kwargs):
    """Get webdriver for given browser

    :type browser: str
    :param browser: Name of browser to use
    :type kwargs: dict
    :param kwargs: Optional arguments
    :rtype: selenium.webdriver
    :returns: Selenium webdriver instance
    """

    driver = None

    if browser.lower() == "firefox":
        driver = FirefoxDriver(**kwargs)

    elif browser.lower() == "chrome":
        driver = ChromeDriver(**kwargs)

    elif browser.lower() == "opera":
        driver = OperaDriver(**kwargs)

    elif browser.lower() == "safari":
        driver = SafariDriver(**kwargs)

    elif browser.lower() == "edge":
        driver = EdgeDriver(**kwargs)

    elif browser.lower() == "ie":
        driver = IeDriver(**kwargs)

    else:
        raise ValueError(f"Invalid browser name[{browser}] specified!")

    return driver.get()
