from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

  button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
  confirm = browser.switch_to.alert.accept()
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)
  input = browser.find_element(By.ID, "answer").send_keys(y)
  submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()


finally:
  time.sleep(10)
  browser.quit()

