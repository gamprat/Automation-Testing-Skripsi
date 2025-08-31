from selenium.webdriver.common.by import By

class ProgramPageLocators:
    PROGRAM_CARD = (By.CSS_SELECTOR, 'a[href="/campaigns/berbagi-pangan-bergizi-untuk-anak-kurang-gizi-LmlS"]')
    BACK_BUTTON = (By.CSS_SELECTOR, 'a[href="/campaigns"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, 'button svg.tabler-icon-filter')
    KEYWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Masukkan kata kunci..."]')
    SELECT_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Pilih unit kerja..."]')
    SELECT_OPTION = (By.XPATH, '//div[@data-combobox-option="true" and contains(., "Lazismu")]')
    CATEGORY_LABEL = (By.CSS_SELECTOR, 'label[for="01jkacy7rhmx1zx3wz2b0rz61t"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="button"]//p[contains(text(),"Terapkan")]')
    RESET_BUTTON = (By.XPATH, '//button[@type="button"]//p[contains(text(),"Reset")]')
    SCROLL_BUTTON = (By.CSS_SELECTOR, 'svg.tabler-icon-arrow-down')