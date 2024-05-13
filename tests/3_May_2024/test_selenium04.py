import pytest
from selenium import webdriver
import logging


def test_login():
    chrome_options = webdriver.ChromeOptions()

    extension_path = "/Users/Admin/Downloads/AdBlock.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("extension_path")

    chrome_options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://app.vwo.com/#/login")
