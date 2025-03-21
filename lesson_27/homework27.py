from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTracker:
    def __init__(self, driver_path=None):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized") 

        self.driver = webdriver.Chrome(executable_path=driver_path, options=options) if driver_path else webdriver.Chrome(options=options)

    def track_parcel(self, tracking_number):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            input_field = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
            )
            input_field.clear()
            input_field.send_keys(tracking_number)
            input_field.send_keys(Keys.RETURN)

            status_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )

            return status_element.text.strip()

        except Exception as e:
            self.driver.save_screenshot("error.png") 
            return f"Помилка Selenium: {e}"

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    tracker = NovaPoshtaTracker()
    tracking_number = "11223344555"  
    status = tracker.track_parcel(tracking_number)
    print(f"Статус посилки: {status}")
    tracker.close()
