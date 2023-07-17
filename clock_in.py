

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_email = "your_email@gmail.com"  # Enter your email here
# This is not secure, but it's just a script for personal use
password = "your_password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("detach", True)


global driver

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://web.jibble.io/login")

driver.maximize_window()

driver.find_element(By.ID, "input-45").send_keys(user_email)
driver.find_element(By.ID, "input-47").send_keys(password)

button = driver.find_elements(By.TAG_NAME, "button")[4]

button.click()


# Wait for page to load before continuing

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.TAG_NAME, "button")
    ))

# Click on the clock in button

x = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "button[data-testid='button-clock-in'][type='button']"))).click()


# Click on the save button
save_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
    (
        By.CSS_SELECTOR, "button[data-testid='right-sidebar-confirm-btn'][type='button']"
    ))).click()
