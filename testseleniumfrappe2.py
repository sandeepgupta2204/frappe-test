from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def dashboard(driver):
    # Print the title of the current page
    print("Page Title after login:", driver.title)

    # Navigate to the '/build' page
    driver.get("https://frappe-uat.dehat.co/app/build")
    time.sleep(3)
    print("Navigated to /build, Page Title:", driver.title)

    # Navigate to the '/users' page
    driver.get("https://frappe-uat.dehat.co/app/users")
    time.sleep(3)
    print("Navigated to /users, Page Title:", driver.title)

    # Navigate to the '/integrations' page
    driver.get("https://frappe-uat.dehat.co/app/integrations")
    time.sleep(3)
    print("Navigated to /integrations, Page Title:", driver.title)
