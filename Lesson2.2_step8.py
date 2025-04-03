from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first = browser.find_element(By.NAME, "firstname" ).send_keys('Dzhaba')
    input_second = browser.find_element(By.NAME, "lastname" ).send_keys('Dzhabavidze')
    input_mail = browser.find_element(By.NAME, "email" ).send_keys('Dzhab@dzhabnex.com')
    file_button = browser.find_element(By.NAME, "file" ).send_keys(os.path.abspath('Шляпа.txt'))
    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
  time.sleep(5)
  browser.quit()