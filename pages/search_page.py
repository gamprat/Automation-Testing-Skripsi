from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.search_page_locators import SearchPageLocators

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org")

    def click_main_area(self):
        self.wait.until(EC.element_to_be_clickable(SearchPageLocators.MAIN_AREA)).click()

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_BUTTON)).click()

    def enter_keyword(self, keyword):
        search_input = self.wait.until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_INPUT))
        search_input.send_keys(keyword)
        return search_input.get_attribute("value")
    
    def click_clear_button(self):
        self.wait.until(EC.element_to_be_clickable(SearchPageLocators.CLEAR_BUTTON)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(SearchPageLocators.BACK_BUTTON)).click()