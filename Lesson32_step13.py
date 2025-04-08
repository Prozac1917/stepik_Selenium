from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, '//div[@class="form-group first_class"]/input')
            input1.send_keys("Жаба")
            input2 = browser.find_element(By.XPATH, '//div[@class="form-group second_class"]/input')
            input2.send_keys("Джабович")
            input3 = browser.find_element(By.XPATH, '//div[@class="form-group third_class"]/input')
            input3.send_keys("Жаба@yan.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        
            browser.quit()

            if __name__== "__main__":
                unittest.main()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, '//div[@class="form-group first_class"]/input')
            input1.send_keys("Жаба")
            input2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
            input2.send_keys("Джабович")
            input3 = browser.find_element(By.XPATH, '//div[@class="form-group third_class"]/input')
            input3.send_keys("Жаба@yan.com")
            time.sleep(10)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        finally:
            browser.quit()

            if __name__== "__main__":
                unittest.main()            