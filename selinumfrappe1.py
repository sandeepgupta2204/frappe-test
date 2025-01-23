from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (example for Chrome)


def login(driver):
        # Open the Frappe login page
        driver.get("https://frappe-uat.dehat.co/app")

        # Allow the page to load
        time.sleep(3)

        # Find the username field, type "Administrator"
        username_field = driver.find_element(By.ID, "login_email")  # Assuming the username field has ID 'login_email'
        username_field.send_keys("Administrator")

        # Find the password field, type "admin"
        password_field = driver.find_element(By.ID, "login_password")  # Assuming the password field has ID 'login_password'
        password_field.send_keys("admin")

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()

        # Wait for the dashboard or next page to load
        time.sleep(5)

        # Print the title of the current page
        print("Page Title after login:", driver.title)
