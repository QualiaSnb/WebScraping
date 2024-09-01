from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://books.toscrape.com/")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/aside/div[2]/ul/li/ul/li[6]/a")))
philosophy_page = driver.find_element(By.XPATH, "/html/body/div/div/div/aside/div[2]/ul/li/ul/li[6]/a")
philosophy_page.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "price_color")))
price_list = driver.find_elements(By.CLASS_NAME, "price_color")

for price in price_list:
    print(price.text)

while True:
    continue