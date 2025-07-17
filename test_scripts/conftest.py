import pytest
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option('detach', True)

@pytest.fixture
def launch():
    driver = Chrome(o)
    driver.get("https://demo.openmrs.org/openmrs/login.htm")
    driver.maximize_window()
    yield driver
    driver.quit()
