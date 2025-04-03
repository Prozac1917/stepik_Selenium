from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    checkbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]').click()
    radio = browser.find_element(By.XPATH, '//input [@id="robotsRule"]').click()
    submit = browser.find_element(By.XPATH, '//button [@type="submit"]').click()
   
finally: 
   time.sleep(10)
   browser.quit()  