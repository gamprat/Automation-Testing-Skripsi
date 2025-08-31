import time
from pages.program_page import ProgramPage
from utils.driver_setup import get_driver, zoom_out_low

class TestProgramPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = ProgramPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_program_page(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(3)
        print("✅ Halaman program berhasil dibuka")

        self.page.click_program_card()
        assert "Berbagi" in self.driver.page_source
        print("✅ Program card berhasil diklik")
        time.sleep(5)

        self.page.click_back_button()
        assert "Program" in self.driver.page_source
        print("✅ Tombol kembali program berhasil diklik")
        time.sleep(5)

        self.page.open_filter()
        print("✅ Filter berhasil diklik")
        time.sleep(5)

        keyword = self.page.enter_keyword("donasi")
        assert keyword == "donasi"
        time.sleep(10)
        print("✅ Keyword 'donasi' berhasil dimasukkan")

        self.page.select_branch()
        time.sleep(5)
        print("✅ Opsi 'Lazismu' berhasil dipilih dari dropdown unit kerja")

        self.page.select_label()
        time.sleep(5)
        print("✅ Label berhasil dipilih")

        self.page.click_submit_filter()
        assert "donasi" in self.driver.page_source or "Donasi" in self.driver.page_source
        print("✅ Filter berhasil diterapkan")

        self.page.open_filter()
        time.sleep(5)
        print("✅ Filter dibuka kembali untuk reset")

        self.page.click_reset_filter()
        time.sleep(5)
        print("✅ Filter berhasil direset")

        self.page.click_submit_filter()
        time.sleep(5)
        print("✅ Filter yang direset berhasil disubmit")

        self.page.scroll_to_bottom()
        time.sleep(5)
        print("✅ Halaman discroll ke bawah")

        self.page.click_scroll_button()
        time.sleep(3)
        print("✅ Tombol muat konten program berhasil diklik")

        self.page.scroll_to_bottom()
        time.sleep(5)
        print("✅ Halaman discroll ulang ke bawah")