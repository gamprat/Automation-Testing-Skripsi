from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.program_detail_page_locators import ProgramDetailPageLocators
import time

class ProgramDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/campaigns/tabungan-surga-6uFj")

    def click_information_tab(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.INFORMATION_TAB)).click()

    def click_news_tab(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.NEWS_TAB)).click()

    def click_donations_tab(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.DONATIONS_TAB)).click()

    def click_fundraisers_tab(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.FUNDRAISERS_TAB)).click()

    def click_share_button(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.SHARE_BUTTON)).click()

    def click_copy_button(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.COPY_BUTTON)).click()

    def handle_share_link(self, href_substring):
        main_window = self.driver.current_window_handle
        share_button = self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.PLATFORM_SHARE_BUTTON(href_substring)))
        share_button.click()
        time.sleep(3)

        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        time.sleep(2)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    def click_close_button(self):
        self.wait.until(EC.element_to_be_clickable(ProgramDetailPageLocators.CLOSE_BUTTON)).click()