from selenium.webdriver.common.by import By

class ProgramDetailPageLocators:
    INFORMATION_TAB = (By.XPATH, '//button[span[text()="Keterangan"]]')
    NEWS_TAB = (By.XPATH, '//button[span[text()="Kabar Terbaru"]]')
    DONATIONS_TAB = (By.XPATH, '//button[span[text()="Donatur"]]')
    FUNDRAISERS_TAB = (By.XPATH, '//button[span[text()="Fundraiser"]]')
    SHARE_BUTTON = (By.XPATH, '//button[span/span[text()="Bagikan"]]')
    COPY_BUTTON = (By.CSS_SELECTOR, 'button svg.tabler-icon-link')
    PLATFORM_SHARE_BUTTON = lambda href: (By.CSS_SELECTOR, f'a[href*="{href}"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button.mantine-Drawer-close')