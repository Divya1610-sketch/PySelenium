import pytest
import logging


from selenium import webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver


def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    LOGGER.info("This is information logs")
    LOGGER.warning("This is Warning logs")
    LOGGER.error("This is Error logs")
    LOGGER.critical("This is critical logs")
    assert "Login - VWO" == driver.title