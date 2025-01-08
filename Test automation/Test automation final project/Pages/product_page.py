import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    rating_stars = (By.XPATH, '//div[@class="interactive-rating"]')
    feedback_box = (By.XPATH, '//*[@id="root"]/div/section/section[1]/div[2]/div/div/div/div/textarea')
    submit_button = (By.XPATH, '//button[@class="new-review-btn new-review-btn-send"]')
    error_message = (By.XPATH, '/html/body/div[1]/div/section/section[1]/div[1]/div/div')
    success_message = (By.XPATH, '/html/body/div[1]/div/section/div[3]/p')
    product_total_element = (By.XPATH, "//div[@class='product-total-container'][1]")

    def verify_date_of_birth(self, dob):
        date_of_birth_input = self.find_element((By.XPATH, '//input[@type="text" and @placeholder="DD-MM-YYYY"]'))
        date_of_birth_input.send_keys(dob)
        confirm_button = self.find_element((By.XPATH, '//button[contains(text(), "Confirm")]'))
        confirm_button.click()

    def click_on_cart(self):
        cart_locator = (By.XPATH, '//div[@class="headerIcon"]')
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(cart_locator)
        )
        cart_icon.click()

    def entering_shop(self):
        shop_locator = (By.XPATH, '//a[@href="/store"]')
        shop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(shop_locator)
        )
        shop.click()

    def add_cart(self):
        add_cart_locator = (
        By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[6]/div/div[2]/div[3]/div/div[2]/button')
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(add_cart_locator)
        )
        cart.click()

    def click_cart_and_buy_product(self):
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
        buy_now = (By.XPATH, '//button[@class="btn-buy-now"]')
        self.click_element(buy_now)

    def select_product_for_rating(self):
        product_locator = (By.XPATH, '//img[@class="card-img-top"]')
        product_1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_locator)
        )
        product_1.click()

    def rate_product(self, stars):
        if stars is None:
            return

        star_locator = (
        By.XPATH, f"//div[@class='new-review-rating-stars']//span[@class='star empty'][position() <= {stars}]")
        star_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(star_locator)
        )
        for star in star_elements:
            star.click()

    def enter_feedback(self, feedback):
        self.enter_text(self.feedback_box, feedback)

    def submit_rating(self):
        self.click_element(self.submit_button)

    def get_error_message(self):
        return self.find_element(self.error_message).text

    def get_success_message(self):
        return self.find_element(self.success_message).text

    def add_products_to_cart(self, target_total):
        tolerance = 0.01
        direction = None

        while True:
            current_total = self.get_product_total()
            if abs(current_total - target_total) <= tolerance:
                print("Debug: Target reached, exiting loop.")
                break
            if current_total < target_total:
                if direction != 'minus':
                    add_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "plus")]'))
                    )
                    add_button.click()
                    direction = 'add'

            elif current_total > target_total:
                if direction != 'add':
                    minus_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "minus")]'))
                    )
                    minus_button.click()
                    direction = 'minus'
            time.sleep(1)  # Short wait to allow the UI to update

    def get_cart_total(self):
        """Retrieve the current cart total from the UI."""
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="total-container"][1]'))
        )
        raw_text = total_element.text.strip()
        # Remove the non-numeric characters (currency symbol and "Total:")
        numeric_text = ''.join(char for char in raw_text if char.isdigit() or char == '.')
        return float(numeric_text)

    def get_product_total(self):
        # Retrieve the product total displayed on the page.
        product_total_element = self.find_element(self.product_total_element)
        product_total_text = product_total_element.text.replace("Product Total:", "").replace("€", "").strip()
        return float(product_total_text)
