import time

import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.constants import PRODUCT_URL, users


@pytest.mark.parametrize("stars, feedback, expected_outcome, user", [
    (1, "Good product!", "You have already reviewed this product.", users[0]),
    (5, "Amazing product!", "You have already reviewed this product.", users[1]),
    (None, None, "Invalid input for the field 'Rating'. Please check your input.", users[2]),
    (4, "x" * 499, "You have already reviewed this product.", users[3]),
    (3, "x" * 501, "Invalid input for the field 'Rating'. Please check your input.", users[4])
])
def test_product_rating(driver, stars, feedback, expected_outcome, user):
    driver.get(PRODUCT_URL)
    driver.maximize_window()
    product_page = ProductPage(driver)
    product_page.verify_date_of_birth("10-12-2000")
    product_page.click_on_cart()
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])
    product_page.entering_shop()
    product_page.click_cart_and_buy_product()
    product_page.entering_shop()
    product_page.select_product_for_rating()
    if stars is None and feedback is None:
        product_page.submit_rating()
        error_message = product_page.get_error_message()
        assert error_message == expected_outcome
    else:
        product_page.rate_product(stars)
        product_page.enter_feedback(feedback)
        product_page.submit_rating()

    if expected_outcome == "You have already reviewed this product.":
        assert product_page.get_success_message() == expected_outcome
    elif expected_outcome == "Invalid input for the field 'Rating'. Please check your input.":
        actual_message = product_page.get_error_message()
        if actual_message != expected_outcome:
            driver.save_screenshot("test_failure_feedback_exceeds_500_chars.png")
        assert actual_message == expected_outcome, f"Expected: {expected_outcome} but got:You have already reviewed this product."
