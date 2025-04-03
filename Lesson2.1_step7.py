from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    

    x_element = browser.find_element(By.ID, "treasure")
    treasure_x = x_element.get_attribute("valuex")
    x = treasure_x
    y = calc(x)
    print(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    inputcheckbox = browser.find_element(By.CSS_SELECTOR, "input.check-input")
    inputcheckbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()