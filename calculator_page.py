from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Controller, Key
from selenium.webdriver.chrome.options import Options
import time

class TestCalculatorPage:
    def setup_method(self, method):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_calculator_profession(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='65%'") 

        income_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="income"]'))
        )
        income_input.send_keys("10000000")
        time.sleep(5)

        additional_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="additionalIncome"]'))
        )
        additional_input.send_keys("1000000")
        time.sleep(5)

        debt_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="debt"]'))
        )
        debt_input.send_keys("200000")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Salurkan Infak"]]'))
        )
        submit_button.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(3)

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]'))
        )
        reset_button.click()
        time.sleep(5)

    def test_calculator_wealth(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='65%'")

        wealth_tab = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-coins'))
        )
        wealth_tab.click()
        time.sleep(5) 

        deposit_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="deposit"]'))
        )
        deposit_input.send_keys("500000")
        time.sleep(5)

        gold_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="gold"]'))
        )
        gold_input.send_keys("200000")
        time.sleep(5)

        property_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="property"]'))
        )
        property_input.send_keys("100000")
        time.sleep(5)

        other_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="otherAssets"]'))
        )
        other_input.send_keys("50000")
        time.sleep(5)

        self.driver.execute_script("window.scrollBy(0, 300);")

        debt_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="debt"]'))
        )
        debt_input.send_keys("200000")
        time.sleep(25)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        click = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header.mantine-AppShell-header'))
        )
        click.click()
        time.sleep(3)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Salurkan Infak"]]'))
        )
        submit_button.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(3)

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]'))
        )
        reset_button.click()
        time.sleep(5)

    def test_calculator_gold(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='65%'")

        gold_tab = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-container'))
        )
        gold_tab.click()
        time.sleep(5) 

        gold_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="gold"]'))
        )
        gold_input.send_keys("2000000")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        click = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header.mantine-AppShell-header'))
        )
        click.click()
        time.sleep(3)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Salurkan Infak"]]'))
        )
        submit_button.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(3)

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]'))
        )
        reset_button.click()
        time.sleep(5)

    def test_calculator_trade(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='65%'")

        trade_tab = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-building-store'))
        )
        trade_tab.click()
        time.sleep(5) 

        current_asset_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="currentAsset"]'))
        )
        current_asset_input.send_keys("2000000")
        time.sleep(5)

        debt_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="debt"]'))
        )
        debt_input.send_keys("2000000")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        click = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header.mantine-AppShell-header'))
        )
        click.click()
        time.sleep(3)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Salurkan Infak"]]'))
        )
        submit_button.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(3)

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]'))
        )
        reset_button.click()
        time.sleep(5)

    def test_calculator_agriculture(self):
        self.driver.get("https://www.sobatlazismu.org/calculator")
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='65%'")

        tab_container = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'mantine-Tabs-list'))
        )

        self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", tab_container)

        agri_tab = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-trees'))
        )
        agri_tab.click()
        time.sleep(5) 

        yield_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="yieldValueInRp"]'))
        )
        yield_input.send_keys("2000000")
        time.sleep(5)

        second_radio = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="self-irrigation"]'))
        )
        second_radio.click()
        time.sleep(5)

        rice_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="ricePricePerKg"]'))
        )
        rice_input.send_keys(Keys.CONTROL + "a")
        rice_input.send_keys(Keys.BACKSPACE)  
        rice_input.send_keys("15000")
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        click = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header.mantine-AppShell-header'))
        )
        click.click()
        time.sleep(3)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Salurkan Infak"]]'))
        )
        submit_button.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(3)

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]'))
        )
        reset_button.click()
        time.sleep(5)