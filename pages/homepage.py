from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.homepage_locators import HomepageLocators

class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org")

    def click_main_area(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.MAIN_AREA)).click()

    def click_cta_button(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.CTA_BUTTON)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.BACK_BUTTON)).click()

    def click_home_button(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.HOME_BUTTON)).click()

    def click_category_program(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.CATEGORY_PROGRAM_BUTTON)).click()

    def close_category_modal(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.CLOSE_MODAL_BUTTON)).click()

    def scroll_by(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels})")

    def click_popular_program(self):
        card = self.wait.until(EC.presence_of_element_located(HomepageLocators.POPULAR_PROGRAM_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)

        program = self.driver.find_element(*HomepageLocators.PROGRAM_CARD_ANCESTOR)
        self.driver.execute_script("arguments[0].click();", program)

    def click_lihat_semua(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.LIHAT_SEMUA)).click()

    def click_heart_icon(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.HEART_ICON)).click()

    def click_selengkapnya(self):
        self.wait.until(EC.element_to_be_clickable(HomepageLocators.SELENGKAPNYA)).click()
