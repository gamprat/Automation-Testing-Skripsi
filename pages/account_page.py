from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key
import os
from dotenv import load_dotenv
import time

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        load_dotenv()
        self.email = os.getenv("SOBATLAZISMU_EMAIL_TEST")

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/account")
    
    def open_profile(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.PROFILE_MENU)).click()

    def update_avatar_input(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.AVATAR_INPUT)).click()
        time.sleep(3)

        keyboard = Controller()
        keyboard.type("C:\\Users\\ACER\\Downloads\\user.svg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)

    def update_name_input(self, amount):
        name_input = self.wait.until(EC.element_to_be_clickable(AccountPageLocators.NAME_INPUT))
        name_input.send_keys(Keys.CONTROL + "a")
        name_input.send_keys(Keys.BACKSPACE)  
        name_input.send_keys(amount)
        return name_input.get_attribute("value")

    def update_phone_input(self, amount):
        phone_input = self.wait.until(EC.element_to_be_clickable(AccountPageLocators.PHONE_INPUT))
        phone_input.send_keys(amount)
        return phone_input.get_attribute("value")

    def update_email_input(self):
        email_input = self.wait.until(EC.element_to_be_clickable(AccountPageLocators.EMAIL_INPUT))
        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.BACKSPACE)  
        email_input.send_keys(self.email)
        return email_input.get_attribute("value")

    def update_address_input(self, amount):
        address_input = self.wait.until(EC.element_to_be_clickable(AccountPageLocators.ADDRESS_INPUT))
        address_input.send_keys(Keys.CONTROL + "a")
        address_input.send_keys(Keys.BACKSPACE)  
        address_input.send_keys(amount)
        return address_input.get_attribute("value")

    def click_submit_profile(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.SUBMIT_BUTTON)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.BACK_BUTTON)).click()

    def update_category_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.CATEGORY_MENU)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.CATEGORY_LABEL_FIRST)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.CATEGORY_LABEL_SECOND)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.SUBMIT_BUTTON)).click()
        time.sleep(2)

    def update_goals_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.GOALS_MENU)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.GOALS_LABEL_FIRST)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.GOALS_LABEL_SECOND)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.SUBMIT_BUTTON)).click()
        time.sleep(2)

    def test_about_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.ABOUT_MENU)).click()

    def test_terms_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.TERMS_MENU)).click()

    def test_privacy_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.PRIVACY_MENU)).click()

    def test_help_menu(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.HELP_MENU)).click()

    def test_account_back_button(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BACK_BUTTON)).click()

    def test_logout(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.CANCEL_CONFIRM_BUTTON)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_CONFIRM_BUTTON)).click()
        time.sleep(2)