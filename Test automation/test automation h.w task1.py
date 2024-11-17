'''
Task 1
Write a script that does the following:
Opens the URL “https://masterschool.com”
 Wait for 2-3 seconds.
Finds the link that has text “Browse Programs” . Hint: Inspect the link to see which appropriate locator can be used.
Click on the link.
Wait for 2 seconds.
Quit.'''



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Set up the WebDriver (replace the path below with the actual path to your WebDriver)'''
driver = webdriver.Chrome()

# Step 2: Open the URL
driver.get("https://masterschool.com")

# Step 3: Wait for 2-3 seconds to allow the page to load
time.sleep(3)

# Step 4: Find the link with the text “Browse Programs” and click it
# We use the LINK_TEXT locator to find the element by its visible text
browse_programs_link = driver.find_element(By.LINK_TEXT, "Unsere Programme")
browse_programs_link.click()

# Step 5: Wait for 2 seconds after clicking
time.sleep(2)


# Step 6: Quit the browser
driver.quit()
