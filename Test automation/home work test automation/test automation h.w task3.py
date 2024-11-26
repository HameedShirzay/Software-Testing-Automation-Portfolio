'''
Task 3
Write a script that automates the login process of any website of your choice. 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Step 1: Setting up the WebDriver
driver = webdriver.Chrome()

# Step 2: Open the URL
driver.get("https://www.facebook.com/login")

# Step 3: Locate the username and password fields and login button
username = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.ID, "loginbutton")


# Step 4: Fill in the credentials
username.send_keys("hameedshirzay9@gmail.com")
password.send_keys("ahmad@1234")


# Step 5: Click the login button
login_button.click()

# Step 6: Wait for a few seconds to let the login process complete
time.sleep(5)

# Step 7: Print the title of the page (to verify successful login)
print("Page Title After Login:", driver.title)


# Step 8: Quit the browser
driver.quit()


