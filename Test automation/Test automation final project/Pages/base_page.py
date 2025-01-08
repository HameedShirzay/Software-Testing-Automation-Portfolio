from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator) )
        element.clear()  # Clear any pre-filled text
        element.send_keys(text)