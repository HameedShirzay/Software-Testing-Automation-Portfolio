from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# intialize web driver
driver = webdriver.Chrome()
try:
    # launch a browser and nevigate the url
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    time.sleep(2)

    # verify home page visiblity
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully.")
    
    
    # To accept cookies (This site asks for consent to use your data)
    driver.find_element(By.XPATH, "//p[contains(text(), 'Consent')]").click()

    # click the product button
    driver.find_element(By.XPATH, "//a[@href='/products']").click()

    # verify all products page visibility
    assert "All Products" in driver.page_source
    print("products page visible successfully")

    # Enter product name in search input and click search button
    search_input = driver.find_element(By.XPATH, '//div[@class="container"]/input[@id="search_product"]')
    search_input.send_keys("dress")
    driver.find_element(By.ID, "submit_search").click()

    # verify Searched Products visiblility
    assert "Searched Products" in driver.page_source
    print("SEARCHED PRODUCTS visible successfully")

    # verify all products realted to search are visible
    product_list = driver.find_elements(By.CLASS_NAME, "productinfo")
    if product_list:
        print(f"All products related to the search are visible. Total products found: {len(product_list)}")
    else:
        print("No products related to the search are visible.")

except Exception as e:
    print("Test Failed", e)

input()    