
class DriverBase:

    def __init__(self, **kwargs):

        self.driver = self.create_driver(**kwargs)

    def get(self):
        """Return the Selenium webdriver instance

        :rtype: selenium.webdriver
        :returns: Selenium webdriver instance
        """

        return self.driver

    def create_driver(self, **kwargs):
        """Create driver instance for given browser

        This method should be implemented by the subclasses.

        :type kwargs: dict
        :param kwargs: Optional arguments
        """

        raise NotImplementedError("Implement this method in the subclass")
