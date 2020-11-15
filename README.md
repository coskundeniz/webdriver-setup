webdriver-setup
===============
Easy to use webdriver instance creation api.

This package prevents manually downloading and setup of the webdriver binaries
by automatically finding and installing the related webdriver binary, and
provides an easy to use instance creation api. It uses
[webdriver_manager](https://pypi.org/project/webdriver-manager/) package.


### Supported browsers

* Firefox
* Chrome
* Opera
* Safari
* Ie
* Edge (Chromium based)


## Installation

`pip install webdriver-setup`


## Usage

```python
from webdriver_setup import get_webdriver_for

# create driver instance
driver = get_webdriver_for("firefox")

# start the browser with the given url
driver.get("https://www.python.org/")

# print the title of the website
print(f"Title: {driver.title}")

# quit browser
driver.quit()
```

You can also pass all the keyworded arguments as you would normally do with the Selenium webdriver instances.

```python
from webdriver_setup import get_webdriver_for
from selenium.webdriver import FirefoxOptions

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")

driver = get_webdriver_for("firefox", options=firefox_options)
```


### WDM Config

If you don't want to see *webdriver_manager* logs, set environment variable "WDM_LOG_LEVEL" to "0"

```python
import os

os.environ["WDM_LOG_LEVEL"] = "0"
```

If you don't pass the `cache_valid_range` option, it will be set to 7 days by default.
You can change it as follows

```python
from webdriver_setup import get_webdriver_for

driver = get_webdriver_for("firefox", cache_valid_range=3)
```

