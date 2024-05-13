from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    # Selenium API -Create Session
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open th browser
    # Navigate to url
    # Command - driver.get(Navigate command to Existing Session)
    driver.get("https://app.vwo.com")

    # Find the Email WebElement and put email id = "abc@gmail.com"
    # Find the Password input box and enter the password = 123
    # Click on the button - Sign in

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username" id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    # Sending the data email and password and clicking on the button
    # sendkeys and click

    email_address_ele.send_keys("dbhagwat001@gmail.com")
    password_ele.send_keys("Divya@1234")

    sign_in_button_ele.click()

    time.sleep(10)

    LOGGER.info('title is'+driver.title)
    assert "Dashboard" in driver.title







