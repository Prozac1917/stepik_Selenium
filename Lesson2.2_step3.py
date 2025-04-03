from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects2.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)

   a_element = browser.find_element(By.ID, "num1")
   a = a_element.text
   b_element = browser.find_element(By.ID, "num2")
   b = b_element.text
   x = str(int(a) + int(b))
   
   select_drop = Select(browser.find_element(By.ID, "dropdown"))
   select_drop.select_by_value(x)
   submit = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
   
finally: 
   time.sleep(10)
   browser.quit()   

