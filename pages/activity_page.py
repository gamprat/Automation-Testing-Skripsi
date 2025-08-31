from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.activity_page_locators import ActivityPageLocators
from selenium.webdriver.common.keys import Keys
import time

class ActivityPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/history")

    def click_zakatmu_menu(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.ZAKATMU_MENU)).click()

    def click_donasimu_menu(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.DONASIMU_MENU)).click()

    def click_history_tab(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.HISTORY_TAB)).click()

    def click_history_card(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.HISTORY_CARD)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.BACK_BUTTON)).click()

    def click_filter_button(self):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.FILTER_BUTTON)).click()

    def add_filter(self, keyword="berbagi"):
        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.KEYWORD_INPUT)).send_keys(keyword)
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.RADIO_BUTTON)).click()
        time.sleep(3)

        dialog = self.wait.until(EC.presence_of_element_located(ActivityPageLocators.DIALOG_FILTER))
        dialog.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.SUBMIT_BUTTON)).click()
        time.sleep(3)

    def reset_filter(self):
        dialog = self.wait.until(EC.presence_of_element_located(ActivityPageLocators.DIALOG_FILTER))
        dialog.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.RESET_BUTTON)).click()
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(ActivityPageLocators.SUBMIT_BUTTON)).click()
        time.sleep(3)