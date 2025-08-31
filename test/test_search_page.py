import time
from pages.search_page import SearchPage
from utils.driver_setup import get_driver

class TestSearchPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = SearchPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_search_page(self):
        self.page.open()
        time.sleep(3)

        self.page.click_main_area()
        time.sleep(3)

        self.page.click_search_button()
        print("✅ Tombol pencarian berhasil diklik")
        time.sleep(3)

        assert self.page.enter_keyword("donasi")
        print("✅ Keyword 'donasi' berhasil dimasukkan")
        time.sleep(5)

        self.page.click_clear_button()
        print("✅ Tombol hapus keyword berhasil diklik")
        time.sleep(3)

        self.page.click_back_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(3)