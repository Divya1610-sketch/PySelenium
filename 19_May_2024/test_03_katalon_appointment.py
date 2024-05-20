import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_katalon_appointment():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID, "btn-login")

    login_button.click()

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))

    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.NAME, "programs").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys(12 / 12 / 1991)
    driver.find_element(By.NAME, "comment").send_keys("I have a fever with 101")

    driver.find_element(By.ID, "btn-book-appointment").click()

    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text

