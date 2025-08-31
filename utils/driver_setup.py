from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("user-data-dir=C:/Users/ACER/SeleniumProfiles/CustomProfile")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver

def zoom_out_medium(driver, level="75%"):
    driver.execute_script(f"document.body.style.zoom='{level}'")

def zoom_out_low(driver, level="65%"):
    driver.execute_script(f"document.body.style.zoom='{level}'")