from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestWeb(unittest.TestCase):
    def test_web1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name = browser.find_element(By.XPATH, '//input[@class="form-control first"][@required]')
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.XPATH, '//input[@class="form-control second"][@required]')
        last_name.send_keys("Petrov")
        email = browser.find_element(By.XPATH, '//input[@class="form-control third"][@required]')
        email.send_keys("text@tv.co")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        a = "Congratulations! You have successfully registered!"
        self.assertEqual(a,welcome_text)
        browser.quit()

    def test_web2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name = browser.find_element(By.XPATH, '//input[@class="form-control first"][@required]')
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.XPATH, '//input[@class="form-control second"][@required]')
        last_name.send_keys("Petrov")
        email = browser.find_element(By.XPATH, '//input[@class="form-control third"][@required]')
        email.send_keys("text@tv.co")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
