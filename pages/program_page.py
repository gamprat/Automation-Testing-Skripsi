from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.program_page_locators import ProgramPageLocators
import time

class ProgramPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/campaigns")

    def click_program_card(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.PROGRAM_CARD)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.BACK_BUTTON)).click()

    def open_filter(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.FILTER_BUTTON)).click()

    def enter_keyword(self, keyword):
        keyword_input = self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.KEYWORD_INPUT))
        keyword_input.send_keys(keyword)
        return keyword_input.get_attribute("value")
    
    def select_branch(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.SELECT_INPUT)).click()
        # time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.SELECT_OPTION)).click()
        # time.sleep(5)

    def select_label(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.CATEGORY_LABEL)).click()

    def click_submit_filter(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.SUBMIT_BUTTON)).click()

    def click_reset_filter(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.RESET_BUTTON)).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_scroll_button(self):
        self.wait.until(EC.element_to_be_clickable(ProgramPageLocators.SCROLL_BUTTON)).click()