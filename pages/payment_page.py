from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.payment_page_locators import PaymentPageLocators
from selenium.webdriver.common.keys import Keys

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/campaigns/berbagi-pangan-bergizi-untuk-anak-kurang-gizi-LmlS")
    
    def click_donate_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.DONATE_BUTTON)).click()

    def choose_nominal(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.NOMINAL_LABEL)).click()

    def enter_name(self, name):
        name_input = self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.NAME_INPUT))
        name_input.send_keys(Keys.CONTROL + "a")
        name_input.send_keys(Keys.BACKSPACE)
        name_input.send_keys(name)
        return name_input.get_attribute("value")

    def enter_phone(self, phone):
        phone_input = self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.PHONE_INPUT))
        phone_input.send_keys(phone)
        return phone_input.get_attribute("value")

    def enter_email(self, email):
        email_input = self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.EMAIL_INPUT))
        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.BACKSPACE)
        email_input.send_keys(email)
        return email_input.get_attribute("value")

    def scroll_dialog(self):
        dialog = self.wait.until(EC.presence_of_element_located(PaymentPageLocators.DIALOG))
        dialog.send_keys(Keys.PAGE_DOWN)

    def enter_notes(self, notes):
        notes_input = self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.NOTES_INPUT))
        notes_input.send_keys(notes)
        return notes_input.get_attribute("value")

    def click_anonymous_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.CHECKBOX)).click()

    def click_lanjutkan_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.LANJUTKAN_BUTTON)).click()

    def click_kembali_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.KEMBALI_BUTTON)).click()

    def click_pembayaran_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.PEMBAYARAN_BUTTON)).click()

    def click_qris_method(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.QRIS_BUTTON)).click()

    def click_va_method(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.VA_BUTTON)).click()

    def click_bank_method(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.BANK_BUTTON)).click()

    def click_download_qris_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.QRIS_DOWNLOAD_BUTTON)).click()

    def click_copy_nominal_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.COPY_NOMINAL_BUTTON)).click()

    def click_copy_account_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.COPY_ACCOUNT_BUTTON)).click()

    def click_check_status_button(self):
        self.wait.until(EC.element_to_be_clickable(PaymentPageLocators.CHECK_STATUS_BUTTON)).click()