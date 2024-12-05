from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Launch browser and navigate to the URL
    driver.get('http://automationexercise.com')
    driver.maximize_window()
    time.sleep(2)


    # Verify home page visibility
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully.")


    # To accept cookies (This site asks for consent to use your data)
    driver.find_element(By.XPATH, "//div//button/p[@class='fc-button-label']").click()


    # Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    # Verify 'New User Signup!' is visible
    assert "New User Signup!" in driver.page_source
    print("'New User Signup!' is visible.")

    # Enter name and email address
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("testuser237@example.com")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    print("new user signed up")
    time.sleep(2)

    # Verify 'ENTER ACCOUNT INFORMATION' is visible
    assert "Enter Account Information" in driver.page_source
    print("'ENTER ACCOUNT INFORMATION' is visible.")
    

    # Fill account information
    driver.find_element(By.ID, "id_gender1").click()  # Select Title (Mr.)
    driver.find_element(By.ID, "name").clear()  # Clear default name
    driver.find_element(By.ID, "name").send_keys("Test User")  # Enter name
    driver.find_element(By.ID, "password").send_keys("Password123")  # Enter password
    Select(driver.find_element(By.ID, "days")).select_by_value("10")  # Select day
    Select(driver.find_element(By.ID, "months")).select_by_value("5")  # Select month
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")  # Select year
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    driver.execute_script("arguments[0].scrollIntoView(true);", newsletter_checkbox)  # Scroll to the checkbox to cover overlay ad
    newsletter_checkbox.click()  # Select newsletter checkbox
    option_checkbox = driver.find_element(By.ID, "optin")
    option_checkbox.click() # Select special offer checkbox
   
    # Fill Address Information
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "company").send_keys("Test Company")
    driver.find_element(By.ID, "address1").send_keys("garden Street")
    driver.find_element(By.ID, "address2").send_keys("Suite 100")
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
    time.sleep(2)

    # Verify 'ACCOUNT CREATED!' is visible
    assert "Account Created!" in driver.page_source
    print("'ACCOUNT CREATED!' is visible.")

    # Click 'Continue' button
    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
    time.sleep(3)

    # Verify 'Logged in as username' is visible
    assert "Test User" in driver.page_source
    print("'Logged in as username' is visible.")


    # Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    time.sleep(2)

    # Verify 'ACCOUNT DELETED!' is visible and continue
    assert "Account Deleted!" in driver.page_source
    print("'ACCOUNT DELETED!' is visible.")
    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

except Exception as e:
    print("Test failed:", e)

input() 