from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    inputcheckbox = browser.find_element(By.CSS_SELECTOR, "input.form-check-input")
    inputcheckbox.click()
    radio = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
