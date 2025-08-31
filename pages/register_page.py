from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.register_page_locators import RegisterPageLocators
import os
from dotenv import load_dotenv

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        load_dotenv()
        self.email = os.getenv("SOBATLAZISMU_EMAIL_TEST")

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/account/register")

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)).click()