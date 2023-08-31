import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:

    browser.get(link)
    print(browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').get_attribute("class"))

    y = calc(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    #print(browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').get_attribute("class"))
    time.sleep(8)
