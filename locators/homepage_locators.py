from selenium.webdriver.common.by import By

class HomepageLocators:
    MAIN_AREA = (By.CLASS_NAME, 'mantine-AppShell-main')
    CTA_BUTTON = (By.LINK_TEXT, 'Donasi Sekarang')
    BACK_BUTTON = (By.CSS_SELECTOR, 'a[href="/campaigns"]')
    HOME_BUTTON = (By.CSS_SELECTOR, 'a[href="/"]')
    CATEGORY_PROGRAM_BUTTON = (By.CSS_SELECTOR, 'div.m_d98df724.mantine-Carousel-slide button.mantine-UnstyledButton-root')
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button.mantine-CloseButton-root')
    POPULAR_PROGRAM_SECTION = (By.XPATH, '//p[text()="Program terpopuler"]')
    POPULAR_PROGRAM_CARD = (By.XPATH, '//p[contains(text(), "Pengembangan SD Unggulan Aisyiyah Bantul")]')
    PROGRAM_CARD_ANCESTOR = (By.XPATH, '//p[contains(text(), "Pengembangan SD Unggulan Aisyiyah Bantul")]/ancestor::a')
    LIHAT_SEMUA = (By.LINK_TEXT, 'Lihat Semua')
    HEART_ICON = (By.CSS_SELECTOR, 'svg.PrayerCarousel_iconHeart___LTGM')
    SELENGKAPNYA = (By.LINK_TEXT, 'Selengkapnya')