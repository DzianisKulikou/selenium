import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:

    browser.get(link)

    #  Вывести значение атрибуда
    #  print(browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').get_attribute("class"))

    x = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    #  print(browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').get_attribute("class"))
    time.sleep(8)
