from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.calculator_page_locators import CalculatorPageLocators
from selenium.webdriver.common.keys import Keys

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")

    def enter_income(self, amount):
        income_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.INCOME_INPUT))
        income_input.send_keys(amount)
        return income_input.get_attribute("value")

    def enter_additional_income(self, amount):
        additional_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.ADDITIONAL_INPUT))
        additional_input.send_keys(amount)
        return additional_input.get_attribute("value")

    def enter_debt(self, amount):
        debt_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.DEBT_INPUT_PROFESSION))
        debt_input.send_keys(amount)
        return debt_input.get_attribute("value")
    
    def get_nilai_zakat_profession(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_PROFESSION_RESULT)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""

    def enter_deposit(self, amount):
        deposit_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.DEPOSIT_INPUT))
        deposit_input.send_keys(amount)
        return deposit_input.get_attribute("value")

    def enter_gold_wealth(self, amount):
        gold_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.GOLD_INPUT_WEALTH))
        gold_input.send_keys(amount)
        return gold_input.get_attribute("value")

    def enter_property(self, amount):
        property_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.PROPERTY_INPUT))
        property_input.send_keys(amount)
        return property_input.get_attribute("value")

    def enter_other_assets(self, amount):
        other_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.OTHER_INPUT))
        other_input.send_keys(amount)
        return other_input.get_attribute("value")

    def enter_debt_wealth(self, amount):
        debt_wealth = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.DEBT_INPUT_WEALTH))
        debt_wealth.send_keys(amount)
        return debt_wealth.get_attribute("value")
    
    def get_nilai_zakat_wealth(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_WEALTH_RESULT)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""

    def enter_gold_container(self, amount):
        gold_input_container = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.GOLD_INPUT_CONTAINER))
        gold_input_container.send_keys(amount)
        return gold_input_container.get_attribute("value")
    
    def get_nilai_zakat_gold_value(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_GOLD_VALUE)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""
        
    def get_nilai_zakat_gold_gram(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_GOLD_GRAM)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""
        
    def get_nilai_zakat_gold_rupiah(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_GOLD_RUPIAH)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""

    def enter_current_assets(self, amount):
        current_assets_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.CURRENT_ASSET_INPUT))
        current_assets_input.send_keys(amount)
        return current_assets_input.get_attribute("value")

    def enter_debt_trade(self, amount):
        debt_input_trade = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.DEBT_INPUT_TRADE))
        debt_input_trade.send_keys(amount)
        return debt_input_trade.get_attribute("value")
    
    def delete_value_trade(self):
        delete_value_trade = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.CURRENT_ASSET_INPUT))
        delete_value_trade.send_keys(Keys.BACKSPACE)
    
    def get_nilai_zakat_trade(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_TRADE_RESULT)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""

    def enter_yield_value(self, amount):
        yield_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.YIELD_INPUT))
        yield_input.send_keys(amount)
        return yield_input.get_attribute("value")

    def enter_rice_price(self, amount):
        rice_price_input = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RICE_PRICE_INPUT))
        rice_price_input.send_keys(Keys.CONTROL + "a")
        rice_price_input.send_keys(Keys.BACKSPACE)  
        rice_price_input.send_keys(amount)
        return rice_price_input.get_attribute("value")
    
    def get_nilai_zakat_agriculture(self):
        try:
            zakat_input = self.driver.find_element(*CalculatorPageLocators.ZAKAT_AGRICULTURE_RESULT)
            return zakat_input.get_attribute("value").strip()
        except Exception as e:
            print(f"❌ Gagal mengambil nilai zakat: {e}")
            return ""

    def click_radio_select(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RADIO_SELECT)).click()

    def scroll_tabs_to_right(self):
        tabs_container = self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.TABS_CONTAINER))
        self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", tabs_container)

    def click_mantine_header(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.MANTINE_HEADER)).click()

    def click_profession_tab(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.PROFESSION_TAB)).click()

    def click_wealth_tab(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.WEALTH_TAB)).click()

    def click_gold_tab(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.GOLD_TAB)).click()
    
    def click_trade_tab(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.TRADE_TAB)).click()

    def click_agriculture_tab(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.AGRI_TAB)).click()

    def salurkan_infak_profession(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_PROFESSION)).click()

    def bayar_zakat_profession(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_PROFESSION_ZAKAT)).click()

    def reset_kalkulator_profession(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RESET_BUTTON_PROFESSION)).click()

    def salurkan_infak_wealth(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_WEALTH)).click()

    def bayar_zakat_wealth(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_WEALTH)).click()

    def reset_kalkulator_wealth(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RESET_BUTTON_WEALTH)).click()

    def salurkan_infak_gold(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_GOLD)).click()

    def reset_kalkulator_gold(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RESET_BUTTON_GOLD)).click()

    def salurkan_infak_trade(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_TRADE)).click()

    def bayar_zakat_trade(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_TRADE)).click()

    def reset_kalkulator_trade(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RESET_BUTTON_TRADE)).click()

    def salurkan_infak_agriculture(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_AGRICULTURE)).click()

    def bayar_zakat_agriculture(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.SUBMIT_BUTTON_AGRICULTURE)).click()

    def reset_kalkulator_agriculture(self):
        self.wait.until(EC.element_to_be_clickable(CalculatorPageLocators.RESET_BUTTON_AGRICULTURE)).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_300_px(self):
        self.driver.execute_script("window.scrollTo(0, 300);")