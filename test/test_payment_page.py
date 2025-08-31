import time
from pages.payment_page import PaymentPage
from utils.driver_setup import get_driver, zoom_out_low

class TestPaymentPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = PaymentPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_payment_qris(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(3)
        
        self.page.click_donate_button()
        print("✅ Tombol Donasi diklik")
        time.sleep(5)

        self.page.choose_nominal()
        print("✅ Nominal dipilih")
        time.sleep(5)

        assert self.page.enter_name("Donatur") == "Donatur"
        print("✅ Nama berhasil diisi")
        time.sleep(5)

        assert self.page.enter_phone("081234567890") == "081234567890"
        print("✅ Nomor telepon diisi")
        time.sleep(5)

        assert self.page.enter_email("donatur@example.com") == "donatur@example.com"
        print("✅ Email berhasil diisi")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        assert self.page.enter_notes("Semoga bermanfaat") == "Semoga bermanfaat"
        print("✅ Doa berhasil diisi")
        time.sleep(5)

        self.page.click_anonymous_checkbox()
        print("✅ Checkbox anonim berhasil diklik")
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik")
        time.sleep(5)

        self.page.click_kembali_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik kembali")
        time.sleep(5)

        self.page.click_pembayaran_button()
        print("✅ Tombol pembayaran berhasil diklik")
        time.sleep(5)

        self.page.click_qris_method()
        print("✅ Metode QRIS berhasil dipilih")
        time.sleep(5)

        self.page.click_download_qris_button()
        print("✅ Berhasil mengunduh kode QRIS")
        time.sleep(5)

        self.page.click_copy_nominal_button()
        print("✅ Berhasil menyalin nominal")
        time.sleep(5)

        self.page.click_check_status_button()
        print("✅ Tombol status pembayaran berhasil diklik")
        time.sleep(5)

    def test_payment_va(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(3)
        
        self.page.click_donate_button()
        print("✅ Tombol Donasi diklik")
        time.sleep(5)

        self.page.choose_nominal()
        print("✅ Nominal dipilih")
        time.sleep(5)

        assert self.page.enter_name("Donatur") == "Donatur"
        print("✅ Nama berhasil diisi")
        time.sleep(5)

        assert self.page.enter_phone("081234567890") == "081234567890"
        print("✅ Nomor telepon diisi")
        time.sleep(5)

        assert self.page.enter_email("donatur@example.com") == "donatur@example.com"
        print("✅ Email berhasil diisi")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        assert self.page.enter_notes("Semoga bermanfaat") == "Semoga bermanfaat"
        print("✅ Doa berhasil diisi")
        time.sleep(5)

        self.page.click_anonymous_checkbox()
        print("✅ Checkbox anonim berhasil diklik")
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik")
        time.sleep(5)

        self.page.click_kembali_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik kembali")
        time.sleep(5)

        self.page.click_pembayaran_button()
        print("✅ Tombol pembayaran berhasil diklik")
        time.sleep(5)

        self.page.click_va_method()
        print("✅ Metode Virtual Account berhasil dipilih")
        time.sleep(5)

        self.page.click_copy_account_button()
        print("✅ Berhasil menyalin nomor rekening")
        time.sleep(5)

        self.page.click_copy_nominal_button()
        print("✅ Berhasil menyalin nominal")
        time.sleep(5)

        self.page.click_check_status_button()
        print("✅ Tombol status pembayaran berhasil diklik")
        time.sleep(5)

    def test_payment_bank(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(3)
        
        self.page.click_donate_button()
        print("✅ Tombol Donasi diklik")
        time.sleep(5)

        self.page.choose_nominal()
        print("✅ Nominal dipilih")
        time.sleep(5)

        assert self.page.enter_name("Donatur") == "Donatur"
        print("✅ Nama berhasil diisi")
        time.sleep(5)

        assert self.page.enter_phone("081234567890") == "081234567890"
        print("✅ Nomor telepon diisi")
        time.sleep(5)

        assert self.page.enter_email("donatur@example.com") == "donatur@example.com"
        print("✅ Email berhasil diisi")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        assert self.page.enter_notes("Semoga bermanfaat") == "Semoga bermanfaat"
        print("✅ Doa berhasil diisi")
        time.sleep(5)

        self.page.click_anonymous_checkbox()
        print("✅ Checkbox anonim berhasil diklik")
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik")
        time.sleep(5)

        self.page.click_kembali_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(5)

        self.page.scroll_dialog()
        time.sleep(5)

        self.page.click_lanjutkan_button()
        print("✅ Tombol lanjutkan berhasil diklik kembali")
        time.sleep(5)

        self.page.click_pembayaran_button()
        print("✅ Tombol pembayaran berhasil diklik")
        time.sleep(5)

        self.page.click_bank_method()
        print("✅ Metode Bank berhasil dipilih")
        time.sleep(5)

        self.page.click_copy_account_button()
        print("✅ Berhasil menyalin nomor rekening")
        time.sleep(5)

        self.page.click_copy_nominal_button()
        print("✅ Berhasil menyalin nominal")
        time.sleep(5)

        self.page.click_check_status_button()
        print("✅ Tombol status pembayaran berhasil diklik")
        time.sleep(5)