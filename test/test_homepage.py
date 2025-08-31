import time
from pages.homepage import Homepage
from utils.driver_setup import get_driver, zoom_out_medium

class TestHomepage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = Homepage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_homepage(self):
        self.page.open()
        time.sleep(5)
        print("✅ Homepage berhasil dibuka")

        self.page.click_main_area()
        time.sleep(5)
        print("✅ Area utama homepage berhasil diklik")

        self.page.click_cta_button()
        assert "program" in self.driver.page_source.lower()
        print("✅ Tombol CTA berhasil diklik dan menuju halaman donasi")
        time.sleep(3)

        self.driver.back()
        print("✅ Berhasil kembali ke beranda")
        time.sleep(3)

        zoom_out_medium(self.driver)
        time.sleep(3)

        self.page.click_category_program()
        print("✅ Tombol kategori program berhasil diklik")
        time.sleep(3)

        self.page.close_category_modal()
        print("✅ Modal kategori program berhasil ditutup")
        time.sleep(3)

        self.page.click_popular_program()
        assert "program" in self.driver.page_source.lower()
        print("✅ Program populer berhasil dibuka")
        time.sleep(3)

        self.page.click_back_button()
        print("✅ Kembali dari halaman program populer")
        time.sleep(3)

        self.page.click_home_button()
        print("✅ Berhasil kembali ke beranda")
        time.sleep(3)

        zoom_out_medium(self.driver)
        time.sleep(3)

        self.page.click_lihat_semua()
        assert "program" in self.driver.page_source.lower()
        print("✅ Tombol 'Lihat Semua' berhasil diklik dan menampilkan daftar program")
        time.sleep(3)

        self.page.click_home_button()
        print("✅ Berhasil kembali ke beranda")
        time.sleep(3)

        self.page.scroll_by(450)
        print("✅ Halaman discroll ke bagian bawah")
        time.sleep(3)

        self.page.click_heart_icon()
        print("✅ Ikon hati berhasil diklik")
        time.sleep(3)

        self.page.click_selengkapnya()
        assert "detail" in self.driver.page_source.lower()
        print("✅ Tombol 'Selengkapnya' berhasil diklik untuk membuka detail berita")
        time.sleep(3)

        self.page.click_home_button()
        print("✅ Tes homepage selesai dengan kembali ke halaman utama")
        time.sleep(3)