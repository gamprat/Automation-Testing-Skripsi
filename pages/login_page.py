from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
import os
from dotenv import load_dotenv

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        load_dotenv()
        self.email = os.getenv("SOBATLAZISMU_EMAIL_TEST")

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/account/login")

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()