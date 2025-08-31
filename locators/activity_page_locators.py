from selenium.webdriver.common.by import By

class ActivityPageLocators:
    ZAKATMU_MENU = (By.XPATH, '//a[.//p[text()="Total zakat kamu"]]')
    DONASIMU_MENU = (By.XPATH, '//a[.//p[text()="Total donasi kamu"]]')
    HISTORY_TAB = (By.XPATH, '//button[.//span[text()="Riwayat"]]')
    HISTORY_CARD = (By.XPATH, '//p[text()="Berbagi Pangan Bergizi Untuk Anak Kurang Gizi"]/ancestor::a')
    BACK_BUTTON = (By.CSS_SELECTOR, 'a[href="/history"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, 'button svg.tabler-icon-filter')
    KEYWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Masukkan kata kunci..."]')
    RADIO_BUTTON = (By.CSS_SELECTOR, 'input[type="radio"][value="current_year"]')
    DIALOG_FILTER = (By.CSS_SELECTOR, 'section[role="dialog"]')
    RESET_BUTTON = (By.XPATH, '//button[@type="button"]//p[contains(text(),"Reset")]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="button"]//p[contains(text(),"Terapkan")]')