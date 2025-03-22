from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time
import os

os.chdir("C:/Users/Siarhei_Shamma/Automation/lesson_26")

alert1_text = ""
alert2_text = ""

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")
time.sleep(2)

frame1 = driver.find_element(By.XPATH, '//*[@id="frame1"]')
driver.switch_to.frame(frame1)

secret_add = driver.find_element(By.XPATH, '//*[@id="input1"]')
secret_add.click()
secret_add.send_keys("Frame1_Secret")
checkbox1 = driver.find_element(By.XPATH, '/html/body/button')
checkbox1.click()

try:
    alert1 = Alert(driver)
    alert1_text = alert1.text
    print(f"Alert text: {alert1_text}")

    alert1.accept()
except NoAlertPresentException:
    print("No alert present after frame 1")

driver.switch_to.default_content()

#frame2

frame2 = driver.find_element(By.XPATH, '//*[@id="frame2"]')
driver.switch_to.frame(frame2)

secret_add = driver.find_element(By.XPATH, '//*[@id="input2"]')
secret_add.click()
secret_add.send_keys("Frame2_Secret")
checkbox2 = driver.find_element(By.XPATH, '/html/body/button')
checkbox2.click()

try:
    alert2 = Alert(driver)
    alert2_text = alert2.text
    print(f"Alert text: {alert2_text}")

    if alert1 == alert2:
        print("It is working good")
    else:
        print(f"The expected alert text is {alert1_text}, but the actual is: {alert2_text}. ")


    alert2.accept()
except NoAlertPresentException:
    print("No alert present after frame 2")

time.sleep(2)
driver.quit()

