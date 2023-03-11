from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    # locators
    EMAIL_FIELD = (By.ID, "Login-email")
    PASSWORD_FIELD = (By.ID, "Login-password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Sign in')]")

    def __init__(self, driver):
        super().__init__(driver)

    def goto(self):
        self.goto_login_page()

    def enter_email(self, email):
        self.driver.element_send_keys(email, self.EMAIL_FIELD)

    def enter_password(self, password):
        self.driver.element_send_keys(password, self.PASSWORD_FIELD)

    def login(self, email=None, password=None):
        self.enter_email(email)
        self.enter_password(password)
        self.driver.element_click(self.LOGIN_BTN)

    def verify_logged_in(self):
        return self.driver.is_element_present(self.header.SIGN_OUT_LINK)

    def verify_login_failed(self):
        INVALID_LOGIN_MSG = (By.XPATH, "//p[contains(text(),"
                                       "'We do not recognise this email or password')]")
        return self.driver.is_element_present(INVALID_LOGIN_MSG)
