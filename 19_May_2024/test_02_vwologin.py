import logging

from selenium import webdriver
from selenium.webdriver.common.by import By



def test_vwologin2():
    LOGGER = logging.getLogger(__name__)
    # Selenium API -Create Session
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open th browser
    # Navigate to url
    # Command - driver.get(Navigate command to Existing Session)
    driver.get("https://app.vwo.com")

    # link = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link = driver.find_element(By.PARTIAL_LINK_TEXT, " free trial")
    link.click()
