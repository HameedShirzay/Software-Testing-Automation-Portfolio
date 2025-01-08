import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.constants import BASE_URL


@pytest.mark.parametrize("cart_total, expected_shipping", [
    (10.00, 5.0),  # Exactly at threshold
    (19.00, 5.0),  # Below threshold
    (20.00, 0.0),  # Well below threshold
    (35.00, 0.0),  # Above threshold
    (5.00, 5.0)  # dynamic total adjustment

])
def test_shipping_cost(driver, cart_total, expected_shipping):
    """Test to verify that the correct shipping cost is applied based on cart total."""

    driver.get(BASE_URL)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver, product_page)  # Pass product_page to CheckoutPage
    login_page = LoginPage(driver)
    # Step 3: Log in to the website
    login_page.click_login_icon()
    login_page.login('hameedshirzay@gmail.com', '1d3f1db63842ba')
    # Step 4: Enter the shop
    product_page.entering_shop()
    product_page.verify_date_of_birth("10-12-2000")
    product_page.add_cart()
    checkout_page.buy_product()
    # Step 5: Add products to the cart dynamically
    product_page.add_products_to_cart(cart_total)
    # Step 6: Retrieve and verify the shipping cost
    actual_shipping_cost = checkout_page.get_shipping_cost()
    # just to finish buying product
    checkout_page.click_buy_product_button()

    print(f"Product total = {cart_total}, Expected shipping = {expected_shipping}, Actual shipping = {actual_shipping_cost}")
    # Assert the shipping cost
    if expected_shipping != actual_shipping_cost:
        driver.save_screenshot("test_failure_dynamic total adjustment.png")
    assert actual_shipping_cost == expected_shipping, f"Expected {expected_shipping}, but got {actual_shipping_cost}"
