from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()


driver.get("https://demo.opencart.com/en-gb?route=common/home")
driver.implicitly_wait(10)

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "search")))

time.sleep(4)

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("ipod")

time.sleep(4)


WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div[2]/div/button")))

search_button = driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/button")
search_button.click()


while True:
    continue