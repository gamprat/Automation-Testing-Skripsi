import time
from pages.program_detail_page import ProgramDetailPage
from utils.driver_setup import get_driver, zoom_out_low

class TestProgramDetailPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = ProgramDetailPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_program_detail_page(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(3)

        self.page.click_information_tab()
        print("✅ Tab Informasi berhasil diklik")
        time.sleep(5)

        self.page.click_news_tab()
        print("✅ Tab Kabar Terbaru berhasil diklik")
        time.sleep(5)

        self.page.click_donations_tab()
        print("✅ Tab Donatur berhasil diklik")
        time.sleep(5)

        self.page.click_fundraisers_tab()
        print("✅ Tab Fundraiser berhasil diklik")
        time.sleep(5)

        self.page.click_share_button()
        print("✅ Tombol bagikan berhasil diklik")
        time.sleep(5)

        self.page.click_copy_button()
        print("✅ Tombol salin tautan berhasil diklik")
        time.sleep(5)

        share_links = [
            'https://wa.me/',
            'https://www.facebook.com/sharer',
            'https://twitter.com/share',
            'https://t.me/share'
        ]

        for href in share_links:
            self.page.handle_share_link(href)
            print(f"✅ Link share {href} berhasil diklik")
            time.sleep(2)

        self.page.click_close_button()
        print("✅ Tombol Tutup popup berhasil diklik")
        time.sleep(5)