from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.constants import BASE_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_icon = (By.XPATH, '//div[@class="headerIcon"]')
        self.email_field = (By.XPATH, '//input[@type="email"]')
        self.password_field = (By.XPATH, '//input[@type="password"]')
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get(BASE_URL)

    def click_login_icon(self):
        login_icon_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_icon))
        login_icon_click.click()

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_field))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_field))
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
