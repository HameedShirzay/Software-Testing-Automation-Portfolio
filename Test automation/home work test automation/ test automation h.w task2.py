'''
Task 2
Write a script that automates the Google search:
Opens the URL "https://www.google.com"
Finds the search bar input element. Use Inspect to see which locator can be used. 
It should send the search term “cats”
Add a delay of 3 seconds.
Print the title of the document (driver).
Quit.
'''
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize the WebDriver
driver = webdriver.Chrome()

# Step 2: Open the URL
driver.get("https://www.google.com")


# step 3: Finds the search bar input element. Use Inspect to see which locator can be used, i used by name locator. 
search_bar = driver.find_element(By.NAME, "q")

# Step 3: Send the search term "cats" to the search bar and submit
search_bar.send_keys("cats")
search_bar.submit()

# Step 4: Add a delay of 3 seconds
time.sleep(3)

# Step 5: Print the title of the document (search results page)
print("Page Title:", driver.title)

# Step 6: Quit the browser
driver.quit()







