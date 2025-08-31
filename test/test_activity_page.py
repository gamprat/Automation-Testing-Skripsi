import time
from pages.activity_page import ActivityPage
from utils.driver_setup import get_driver, zoom_out_low

class TestActivityPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = ActivityPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_activity_summary(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.click_zakatmu_menu()
        print("✅ Menu zakatmu berhasil diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.click_donasimu_menu()
        print("✅ Menu donasimu berhasil diklik")
        time.sleep(5)

    def test_activity_history(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.click_history_tab()
        print("✅ Tab riwayat berhasil diklik")
        time.sleep(5)

        self.page.click_history_card()
        print("✅ Card riwayat berhasil diklik")
        time.sleep(5)

        self.page.click_back_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(5)

        self.page.click_history_tab()
        print("✅ Tab riwayat berhasil diklik kembali")
        time.sleep(5)

        self.page.click_filter_button()
        print("✅ Tombol filter berhasil diklik")
        time.sleep(5)
        
        self.page.add_filter()
        print("✅ Berhasil filter data")
        time.sleep(5)

        self.page.click_filter_button()
        print("✅ Tombol filter berhasil diklik kembali")
        time.sleep(5)

        self.page.reset_filter()
        print("✅ Berhasil reset filter")
        time.sleep(5)