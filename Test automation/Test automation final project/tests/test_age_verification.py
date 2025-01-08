import pytest

from pages import product_page
from pages.age_verification_page import AgeVerificationPage
from pages.product_page import ProductPage
from utils.constants import TODAY_DATE_MINUS_18, TODAY_DATE_MINUS_17, BASE_URL, PRODUCT_URL


@pytest.mark.parametrize("dob, expected_outcome", [
    (TODAY_DATE_MINUS_18, "access"),  # Exactly 18 years old
    (TODAY_DATE_MINUS_17, "error"),  # Under 18
    ("06/01/2006", "access"),  # above age
    ("99/99/9999", "error"),  # Invalid date
    ("", "error")  # Blank input
])
def test_age_verification(driver, dob, expected_outcome):
    driver.get(PRODUCT_URL)
    driver.maximize_window()
    age_verification_page = AgeVerificationPage(driver)
    age_verification_page.verify_age(dob)

    if expected_outcome == "access":
        assert "Market Mate" in driver.title
    elif expected_outcome == "You are underage. You can still browse the site, but you will not be able to view alcohol products.":
        assert age_verification_page.get_error_message()
