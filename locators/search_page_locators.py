from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[data-sentry-element="TextInput"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Cari"]')
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'button .tabler-icon-x')
    BACK_BUTTON = (By.CSS_SELECTOR, 'button .tabler-icon-arrow-left')
    MAIN_AREA = (By.CLASS_NAME, 'mantine-AppShell-main')