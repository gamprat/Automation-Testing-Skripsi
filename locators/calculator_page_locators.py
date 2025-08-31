from selenium.webdriver.common.by import By

class CalculatorPageLocators:
    # PROFESSION TAB
    INCOME_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="income"]')
    ADDITIONAL_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="additionalIncome"]')
    DEBT_INPUT_PROFESSION = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="debt"]')
    ZAKAT_PROFESSION_RESULT = (By.XPATH,'//label[contains(.,"Nilai Zakat")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatProfession.tsx"]')

    # WEALTH TAB
    DEPOSIT_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="deposit"]')
    GOLD_INPUT_WEALTH = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="gold"]')
    PROPERTY_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="property"]')
    OTHER_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="otherAssets"]')
    DEBT_INPUT_WEALTH = (By.CSS_SELECTOR, 'input[data-sentry-source-file="ZakatWealth.tsx"][data-path="debt"]')
    ZAKAT_WEALTH_RESULT = (By.XPATH,'//label[contains(.,"Nilai Zakat")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatWealth.tsx"]')

    # GOLD TAB
    GOLD_INPUT_CONTAINER = (By.CSS_SELECTOR, 'input[data-sentry-source-file="ZakatGold.tsx"][data-path="gold"]')
    ZAKAT_GOLD_VALUE = (By.XPATH,'//label[contains(.,"Nilai Emas dalam Rupiah")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatGold.tsx"]')
    ZAKAT_GOLD_GRAM = (By.XPATH,'//label[contains(.,"Nilai Zakat dalam gram")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatGold.tsx"]')
    ZAKAT_GOLD_RUPIAH = (By.XPATH,'//label[contains(.,"Nilai Zakat dalam Rupiah")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatGold.tsx"]')

    # TRADE TAB
    CURRENT_ASSET_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="currentAsset"]')
    DEBT_INPUT_TRADE = (By.CSS_SELECTOR, 'input[data-sentry-source-file="ZakatTrade.tsx"][data-path="debt"]')
    ZAKAT_TRADE_RESULT = (By.XPATH,'//label[contains(.,"Nilai Zakat")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatTrade.tsx"]')

    # AGRICULTURE TAB
    YIELD_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="yieldValueInRp"]')
    RICE_PRICE_INPUT = (By.CSS_SELECTOR, 'input[id^="mantine-"][data-path="ricePricePerKg"]')
    RADIO_SELECT = (By.XPATH, '//input[@type="radio" and @value="self-irrigation"]')
    ZAKAT_AGRICULTURE_RESULT = (By.XPATH,'//label[contains(.,"Nilai Zakat")]/following-sibling::div//input[@readonly and @data-sentry-source-file="ZakatAgriculture.tsx"]')

    # TABS
    TABS_CONTAINER = (By.CLASS_NAME, 'mantine-Tabs-list')
    PROFESSION_TAB = (By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-briefcase')
    WEALTH_TAB = (By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-coins')
    GOLD_TAB = (By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-container')
    TRADE_TAB = (By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-building-store')
    AGRI_TAB = (By.CSS_SELECTOR, 'button .tabler-icon.tabler-icon-trees')

    # BUTTON
    SUBMIT_BUTTON_PROFESSION = (By.XPATH, '//button[.//span[text()="Salurkan Infak"]]')
    SUBMIT_BUTTON_PROFESSION_ZAKAT = (By.XPATH, '//button[.//span[text()="Bayar Zakat"]]')
    RESET_BUTTON_PROFESSION = (By.XPATH, '//button[.//span[text()="Reset Kalkulator"]]')
    SUBMIT_BUTTON_WEALTH = (By.CSS_SELECTOR, 'button[data-sentry-source-file="ZakatWealth.tsx"]')
    RESET_BUTTON_WEALTH = (By.CSS_SELECTOR, 'button[data-variant="outline"][type="button"][data-sentry-source-file="ZakatWealth.tsx"]')
    SUBMIT_BUTTON_GOLD = (By.CSS_SELECTOR, 'button[data-sentry-source-file="ZakatGold.tsx"]')
    RESET_BUTTON_GOLD = (By.CSS_SELECTOR, 'button[data-variant="outline"][type="button"][data-sentry-source-file="ZakatGold.tsx"]')
    SUBMIT_BUTTON_TRADE = (By.CSS_SELECTOR, 'button[data-sentry-source-file="ZakatTrade.tsx"]')
    RESET_BUTTON_TRADE = (By.CSS_SELECTOR, 'button[data-variant="outline"][type="button"][data-sentry-source-file="ZakatTrade.tsx"]')
    SUBMIT_BUTTON_AGRICULTURE = (By.CSS_SELECTOR, 'button[data-sentry-source-file="ZakatAgriculture.tsx"]')
    RESET_BUTTON_AGRICULTURE = (By.CSS_SELECTOR, 'button[data-variant="outline"][type="button"][data-sentry-source-file="ZakatAgriculture.tsx"]')

    # CLICKABLE
    MANTINE_HEADER = (By.CSS_SELECTOR, 'header.mantine-AppShell-header')