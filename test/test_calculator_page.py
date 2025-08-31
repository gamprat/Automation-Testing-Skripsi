import time
import math
from pages.calculator_page import CalculatorPage
from utils.driver_setup import get_driver, zoom_out_low

class TestCalculatorPage:
    def setup_method(self):
        self.driver = get_driver()
        self.page = CalculatorPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_calculator_profession(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        assert self.page.enter_income("10000000000") == "Rp010.000.000.000"
        print("✅ Penghasilan berhasil diinput")

        assert self.page.enter_additional_income("1000000") == "Rp01.000.000"
        print("✅ Penghasilan tambahan berhasil diinput")

        assert self.page.enter_debt("200000") == "Rp0200.000"
        print("✅ Hutang berhasil diinput")

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_profession()
        print(f"ℹ️ Nilai zakat ditampilkan: {zakat_value}")

        expected_zakat = (10000000000 + 1000000 - 200000) * 0.025
        expected_zakat_str = f"Rp{expected_zakat:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat yang diharapkan: {expected_zakat_str}")
        
        assert zakat_value == expected_zakat_str, "❌ Nilai zakat tidak sesuai"
        print("✅ Nilai zakat sesuai perhitungan")

        self.page.bayar_zakat_profession()
        print("✅ Tombol salurkan infak profesi diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.reset_kalkulator_profession()
        print("✅ Kalkulator profesi berhasil direset")
        time.sleep(5)

    def test_calculator_wealth(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.click_wealth_tab()
        print("✅ Tab harta berhasil diklik")
        time.sleep(5)

        assert self.page.enter_deposit("200000000") == "Rp0200.000.000"
        print("✅ Deposito berhasil diinput")

        assert self.page.enter_gold_wealth("1000000") == "Rp01.000.000"
        print("✅ Emas berhasil diinput")

        assert self.page.enter_property("7000000") == "Rp07.000.000"
        print("✅ Properti berhasil diinput")

        assert self.page.enter_other_assets("90000000") == "Rp090.000.000"
        print("✅ Aset lain berhasil diinput")

        self.page.scroll_to_300_px()
        time.sleep(5)

        assert self.page.enter_debt_wealth("15000000") == "Rp015.000.000"
        print("✅ Hutang berhasil diinput")

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_wealth()
        print(f"ℹ️ Nilai zakat ditampilkan: {zakat_value}")

        expected_zakat = (200000000 + 1000000 + 7000000 + 90000000 - 15000000) * 0.025
        expected_zakat_str = f"Rp{expected_zakat:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat yang diharapkan: {expected_zakat_str}")
        
        assert zakat_value == expected_zakat_str, "❌ Nilai zakat tidak sesuai"
        print("✅ Nilai zakat sesuai perhitungan")

        self.page.click_mantine_header()
        time.sleep(5)

        self.page.bayar_zakat_wealth()
        print("✅ Tombol salurkan infak (harta) diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.scroll_to_top()
        time.sleep(5)

        self.page.click_wealth_tab()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        self.page.reset_kalkulator_wealth()
        print("✅ Kalkulator harta berhasil direset")
        time.sleep(5)

    def test_calculator_gold(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.click_gold_tab()
        print("✅ Tab emas berhasil diklik")
        time.sleep(5)

        self.page.enter_gold_container("85") == "085"
        print("✅ Jumlah emas berhasil diinput")
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_gold_value()
        print(f"ℹ️ Nilai emas dalam rupiah yang ditampilkan: {zakat_value}")

        zakat_gram = self.page.get_nilai_zakat_gold_gram()
        print(f"ℹ️ Nilai zakat dalam gram yang ditampilkan: {zakat_gram}")

        zakat_rupiah = self.page.get_nilai_zakat_gold_rupiah()
        print(f"ℹ️ Nilai zakat dalam rupiah yang ditampilkan: {zakat_rupiah}")

        expected_zakat_value = 85 * 1858519
        expected_zakat_str_value = f"Rp{expected_zakat_value:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai emas dalam rupiah yang diharapkan: {expected_zakat_str_value}")

        expected_zakat_gram = 0.025 * 85
        expected_zakat_str_gram = f"{expected_zakat_gram:,.3f}gr".replace(",", "X").replace(".", ",").replace("X", ".")  

        print(f"🎯 Nilai zakat dalam gram yang diharapkan: {expected_zakat_str_gram}")

        expected_zakat_rupiah = 0.025 * 85 * 1858519
        expected_zakat_rounded = math.ceil(expected_zakat_rupiah)
        expected_zakat_str_rupiah = f"Rp{expected_zakat_rounded:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat dalam rupiah yang diharapkan: {expected_zakat_str_rupiah}")

        assert zakat_value == expected_zakat_str_value, "❌ Nilai emas dalam rupiah tidak sesuai"
        print("✅ Nilai emas dalam rupiah sesuai perhitungan")
        
        assert zakat_gram == expected_zakat_str_gram, "❌ Nilai zakat dalam gram tidak sesuai"
        print("✅ Nilai zakat dalam gram sesuai perhitungan")

        assert zakat_rupiah == expected_zakat_str_rupiah, "❌ Nilai zakat dalam rupiah tidak sesuai"
        print("✅ Nilai zakat dalam rupiah sesuai perhitungan")

        self.page.click_mantine_header()
        time.sleep(5)

        self.page.salurkan_infak_gold()
        print("✅ Tombol salurkan infak (emas) diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.scroll_to_top()
        time.sleep(5)

        self.page.click_gold_tab()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        self.page.reset_kalkulator_gold()
        print("✅ Kalkulator emas berhasil direset")
        time.sleep(5)

    def test_calculator_trade(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.click_trade_tab()
        print("✅ Tab perdagangan berhasil diklik")
        time.sleep(5)

        self.page.enter_current_assets("1900000000") == "Rp01.900.000.000"
        print("✅ Aset berhasil diinput")
        time.sleep(5)

        self.page.enter_debt_trade("9000000") == "Rp09.000.000"
        print("✅ Hutang berhasil diinput")
        time.sleep(5)

        self.page.delete_value_trade()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_trade()
        print(f"ℹ️ Nilai zakat ditampilkan: {zakat_value}")

        expected_zakat = (190000000 - 9000000) * 0.025
        expected_zakat_str = f"Rp{expected_zakat:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat yang diharapkan: {expected_zakat_str}")
        
        assert zakat_value == expected_zakat_str, "❌ Nilai zakat tidak sesuai"
        print("✅ Nilai zakat sesuai perhitungan")

        self.page.click_mantine_header()
        time.sleep(5)

        self.page.bayar_zakat_trade()
        print("✅ Tombol salurkan infak (perdagangan) diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.scroll_to_top()
        time.sleep(5)

        self.page.click_trade_tab()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        self.page.reset_kalkulator_trade()
        print("✅ Kalkulator perdagangan berhasil direset")
        time.sleep(5)

    def test_calculator_agriculture(self):
        self.page.open()
        zoom_out_low(self.driver)
        time.sleep(5)

        self.page.scroll_tabs_to_right()
        time.sleep(5)

        self.page.click_agriculture_tab()
        print("✅ Tab pertanian berhasil diklik")
        time.sleep(5)

        self.page.enter_yield_value("7000000") == "Rp07.000.000"
        print("✅ Pendapatan panen berhasil diinput")
        time.sleep(5)

        self.page.enter_rice_price("10000") == "Rp10000"
        print("✅ Harga gabah berhasil diinput")
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_agriculture()
        print(f"ℹ️ Nilai zakat ditampilkan: {zakat_value}")

        expected_zakat = 7000000 * 0.10
        expected_zakat_str = f"Rp{expected_zakat:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat yang diharapkan: {expected_zakat_str}")
        
        assert zakat_value == expected_zakat_str, "❌ Nilai zakat tidak sesuai"
        print("✅ Nilai zakat sesuai perhitungan")

        self.page.click_mantine_header()
        time.sleep(5)

        self.page.bayar_zakat_agriculture()
        print("✅ Tombol salurkan infak (pertanian) diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.scroll_to_top()
        time.sleep(5)

        self.page.scroll_tabs_to_right()
        time.sleep(5)

        self.page.click_agriculture_tab()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        self.page.reset_kalkulator_agriculture()
        print("✅ Kalkulator pertanian berhasil direset")
        time.sleep(5)

        self.page.enter_yield_value("7000000") == "Rp07.000.000"
        print("✅ Pendapatan panen berhasil diinput")
        time.sleep(5)

        self.page.click_radio_select()
        print("✅ Tombol radio berhasil dipilih")
        time.sleep(5)

        self.page.enter_rice_price("10000") == "Rp10000"
        print("✅ Harga gabah berhasil diinput")
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        zakat_value = self.page.get_nilai_zakat_agriculture()
        print(f"ℹ️ Nilai zakat ditampilkan: {zakat_value}")

        expected_zakat = 7000000 * 0.05
        expected_zakat_str = f"Rp{expected_zakat:,.0f}".replace(",", ".")  

        print(f"🎯 Nilai zakat yang diharapkan: {expected_zakat_str}")
        
        assert zakat_value == expected_zakat_str, "❌ Nilai zakat tidak sesuai"
        print("✅ Nilai zakat sesuai perhitungan")

        self.page.click_mantine_header()
        time.sleep(5)

        self.page.bayar_zakat_agriculture()
        print("✅ Tombol salurkan infak (pertanian) diklik")
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        self.page.scroll_to_top()
        time.sleep(5)

        self.page.scroll_tabs_to_right()
        time.sleep(5)

        self.page.click_agriculture_tab()
        time.sleep(5)

        self.page.scroll_to_bottom()
        time.sleep(5)

        self.page.reset_kalkulator_agriculture()
        print("✅ Kalkulator pertanian berhasil direset")
        time.sleep(5)