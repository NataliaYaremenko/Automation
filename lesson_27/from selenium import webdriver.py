from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: Run in headless mode
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://tracking.novaposhta.ua/#/uk")
    
    # Wait for input field
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Введіть номер накладної']"))
    )
    input_field.send_keys("YOUR_TRACKING_NUMBER_HERE")

    # Click search button
    search_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='search-btn']"))
    )
    search_button.click()

    # Wait for status
    status_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header__status-text"))
    )
    print(f"Статус посилки: {status_text.text}")

except Exception as e:
    print(f"Помилка Selenium: {e}")

finally:
    driver.quit()  # Ensure browser closes
