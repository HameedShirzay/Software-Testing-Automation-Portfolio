import time

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    shipping_cost_element = (By.XPATH, "//div[@class='shipment-container'][1]")
    total_cost_element = (By.XPATH, "//div[@class='total-container']/h5")

    def __init__(self, driver, product_page):
        super().__init__(driver)
        self.product_page = product_page

    def buy_product(self):
        product_to_buy = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="headerIcon"][3]'))
        )
        product_to_buy.click()
        street_name_locator = (By.XPATH, '//input[@class="shipment-input" and @placeholder="Street Address"]')
        self.enter_text(street_name_locator, 'philip street')
        city_locator = (By.XPATH, '//input[@class="shipment-input" and @placeholder="City"]')
        self.enter_text(city_locator, 'Ansbach')
        postal_code_locator = (By.XPATH, '//input[@class="shipment-input" and @placeholder="Postal Code"]')
        self.enter_text(postal_code_locator, 91522)
        card_number_locator = (By.XPATH, '//input[@class="payment-input" and @placeholder="Card number"]')
        self.enter_text(card_number_locator, 1234566778)
        name_on_card_locator = (By.XPATH, '//input[@class="payment-input" and @placeholder="Name on card"]')
        self.enter_text(name_on_card_locator, 'Hameed')
        expiration_locator = (By.XPATH, '//input[@class="payment-input" and @placeholder="Expiration"]')
        self.enter_text(expiration_locator, '12-2030')
        cvv_locator = (By.XPATH, '//input[@class="payment-input" and @placeholder="Cvv"]')
        self.enter_text(cvv_locator, 123)

    def click_buy_product_button(self):
        buy_now = (By.XPATH, '//button[@class="btn-buy-now"]')
        self.click_element(buy_now)

    def get_shipping_cost(self):
        """Wait for the shipping cost to update and then retrieve it."""
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.shipping_cost_element, "Shipment:")
        )
        shipping_cost_text = self.find_element(self.shipping_cost_element).text
        # using regex to extract the first numeric value because of (shipment:) and € sign
        import re
        match = re.search(r'\d+', shipping_cost_text)
        if match:
            return float(match.group())  # Convert the extracted numeric part to a float
        # Return 0.0 if no numeric value is found
        return 0.0


