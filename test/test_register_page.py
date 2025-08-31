import time
from pages.register_page import RegisterPage
from utils.driver_setup import get_driver

class TestRegisterPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = RegisterPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_register_page(self):
        self.page.open()
        time.sleep(5)

        self.page.click_register_button()
        time.sleep(15)
        assert "Google" in self.driver.page_source or "accounts.google.com" in self.driver.current_url
        print("✅ Berhasil mendaftar menggunakan akun Google")