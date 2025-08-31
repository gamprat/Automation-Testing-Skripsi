import time
from pages.account_page import AccountPage
from utils.driver_setup import get_driver, zoom_out_low

class TestAccountPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = AccountPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_account_profile(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.open_profile()
        print("✅ Berhasil membuka halaman profile")
        time.sleep(5)

        self.page.update_avatar_input()
        print("✅ Avatar berhasil diperbarui")
        time.sleep(5)

        assert self.page.update_name_input("User Tester") == "User Tester"
        print("✅ Nama berhasil diinput")
        time.sleep(5)

        assert self.page.update_phone_input("08123456789") == "08123456789"
        print("✅ Nomor telepon berhasil diinput")
        time.sleep(5)

        self.page.update_email_input()
        print("✅ Email berhasil diinput")
        time.sleep(5)

        assert self.page.update_address_input("Jl. Jendral Sudirman") == "Jl. Jendral Sudirman"
        print("✅ Alamat berhasil diinput")
        time.sleep(5)

        self.page.click_submit_profile()
        print("✅ Berhasil menyimpan profil")
        time.sleep(5)

        self.page.click_back_button()
        print("✅ Tombol kembali berhasil diklik")
        time.sleep(5)

    def test_account_tab(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.update_category_menu()
        print("✅ Menu kategori berhasil diperbarui")
        time.sleep(5)

        self.page.update_goals_menu()
        print("✅ Menu sdgs berhasil diperbarui")
        time.sleep(5)

    def test_account_nav(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.test_about_menu()
        print("✅ Menu tentang sobatlazismu berhasil diklik")
        time.sleep(5)

        self.page.test_account_back_button()
        print("✅ Berhasil kembali ke halaman akun")
        time.sleep(5)

        self.page.test_terms_menu()
        print("✅ Menu syarat dan ketentuan berhasil diklik")
        time.sleep(5)

        self.page.test_account_back_button()
        print("✅ Berhasil kembali ke halaman akun")
        time.sleep(5)

        self.page.test_privacy_menu()
        print("✅ Menu kebijakan privasi berhasil diklik")
        time.sleep(5)

        self.page.test_account_back_button()
        print("✅ Berhasil kembali ke halaman akun")
        time.sleep(5)

        self.page.test_help_menu()
        print("✅ Menu bantuan berhasil diklik")
        time.sleep(5)

        self.page.test_account_back_button()
        print("✅ Berhasil kembali ke halaman akun")
        time.sleep(5)

        self.page.test_logout()
        time.sleep(10)