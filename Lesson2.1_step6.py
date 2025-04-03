from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots radio: ", robots_checked)
assert robots_checked is None

time.sleep(10)

submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
submit_disabled = submit_button.get_attribute("disabled")
print("value of submit button: ", submit_disabled)
assert submit_disabled is not None
 