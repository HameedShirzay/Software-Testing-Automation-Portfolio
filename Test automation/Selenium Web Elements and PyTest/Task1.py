from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")


# Handle the cookies banner if it appears
cookies_accept_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='L2AGLb']"))
)
cookies_accept_button.click()
print("Cookies banner accepted.")
time.sleep(2)


# Wait for the search bar to become visible
search_bar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
print("Search bar is visible.")
time.sleep(2)


# Enter the search term "istqb"
search_term = "istqb"
search_bar.send_keys(search_term)
print(f"Entered search term: {search_term}")
time.sleep(2)


# Wait for the first dropdown suggestion to appear
first_suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']/li[1]"))
)
print("First suggestion found.")
time.sleep(2)

# Click the first suggestion
first_suggestion.click()
print("First suggestion clicked successfully!")

# Browser remains open for manual inspection
print("Task completed. Browser will remain open for inspection.")
input("please enter to exit the window")