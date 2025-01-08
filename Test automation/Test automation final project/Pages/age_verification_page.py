from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AgeVerificationPage(BasePage):
    dob_field = (By.XPATH, '//input[@type="text" and @placeholder="DD-MM-YYYY"]')
    confirm_button = (By.ID, '//button[contains(text(), "Confirm")]')
    error_message = (By.XPATH, '//div[@role="status" @class="go3958317564"]')

    def verify_age(self, dob):
        date_of_birth_input = self.find_element((By.XPATH, '//input[@type="text" and @placeholder="DD-MM-YYYY"]'))
        date_of_birth_input.send_keys(dob)
        confirm_button = self.find_element((By.XPATH, '//button[contains(text(), "Confirm")]'))
        confirm_button.click()

    def get_error_message(self):
        return self.find_element(self.error_message).text
