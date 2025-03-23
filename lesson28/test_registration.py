import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

def test_user_registration(driver):
    driver.get("https://qauto2.forstudy.space/")
    wait = WebDriverWait(driver, 10)
    
    sign_up_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Up') or contains(text(), 'Реєстрація')]")))
    sign_up_btn.click()
    
    random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
    test_email = f"test.{random_string}@example.com"
    test_password = f"Password{random_string}123"
    
    wait.until(EC.visibility_of_element_located((By.ID, "signupName"))).send_keys(f"Test {random_string}")
    driver.find_element(By.ID, "signupLastName").send_keys(f"User {random_string}")
    driver.find_element(By.ID, "signupEmail").send_keys(test_email)
    driver.find_element(By.ID, "signupPassword").send_keys(test_password)
    driver.find_element(By.ID, "signupRepeatPassword").send_keys(test_password)
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Register') or contains(text(), 'Зареєструватися')]").click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Garage') or contains(text(), 'Гараж')]")))
    
    user_email_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'header_email')]")))
    assert test_email in user_email_element.text, f"Expected email {test_email} not found in: {user_email_element.text}"