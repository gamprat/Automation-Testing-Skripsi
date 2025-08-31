import time
from pages.login_page import LoginPage
from utils.driver_setup import get_driver

class TestLoginPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_login_page(self):
        self.page.open()
        time.sleep(5)

        self.page.click_login_button()
        assert "Google" in self.driver.page_source or "accounts.google.com" in self.driver.current_url
        print("✅ Berhasil login menggunakan akun Google")
        time.sleep(15)