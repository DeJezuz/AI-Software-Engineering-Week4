"""
Selenium login test automation.
File: code/task2_selenium_login.py

Notes:
- Configure LOGIN_URL and credential values before running.
- Uses webdriver-manager to automatically download the right driver.
- Saves screenshot to report/figures/login_test_result.png
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# --- CONFIGURE THESE ---
LOGIN_URL = "https://example.com/login"   # <-- Replace with real URL
VALID_USERNAME = "valid_user"             # <-- Replace
VALID_PASSWORD = "valid_pass"             # <-- Replace
INVALID_USERNAME = "bad_user"
INVALID_PASSWORD = "bad_pass"

# CSS/XPath selectors — replace with the right ones for your page
USERNAME_SELECTOR = (By.NAME, "username")
PASSWORD_SELECTOR = (By.NAME, "password")
SUBMIT_XPATH = "//button[@type='submit']"
SUCCESS_INDICATOR = (By.ID, "logout")  # example success indicator: element present after login
ERROR_CLASS = "error"                  # element class used for login errors

# --- END CONFIG ---

OUTPUT_DIR = os.path.join("report", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_login_test(driver, username, password):
    driver.get(LOGIN_URL)
    time.sleep(1)
    # Clear & fill username
    uel = driver.find_element(*USERNAME_SELECTOR)
    uel.clear()
    uel.send_keys(username)
    pel = driver.find_element(*PASSWORD_SELECTOR)
    pel.clear()
    pel.send_keys(password)
    driver.find_element(By.XPATH, SUBMIT_XPATH).click()
    time.sleep(2)

    # Heuristics to determine success: presence of known logout element or URL change
    if SUCCESS_INDICATOR and driver.find_elements(*SUCCESS_INDICATOR):
        return True
    page = driver.page_source.lower()
    if ERROR_CLASS and ERROR_CLASS in page:
        return False
    # fallback: check URL changed (common pattern)
    if "login" not in driver.current_url:
        return True
    return False

def main():
    options = Options()
    options.headless = True  # set False to watch the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        valid_result = run_login_test(driver, VALID_USERNAME, VALID_PASSWORD)
        # For invalid test we expect login to fail; we invert the return for "correctness"
        invalid_result = not run_login_test(driver, INVALID_USERNAME, INVALID_PASSWORD)

        print("Valid credentials test passed:", valid_result)
        print("Invalid credentials test passed:", invalid_result)

        # Save screenshot
        screenshot_path = os.path.join(OUTPUT_DIR, "login_test_result.png")
        driver.save_screenshot(screenshot_path)
        print("Screenshot saved to:", screenshot_path)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
