from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

browser.get(link)
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

button_wait = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"100"))
button = browser.find_element(By.ID, "book")
button_wait = button.click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.ID, "answer").send_keys(y)
submit = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(10)
