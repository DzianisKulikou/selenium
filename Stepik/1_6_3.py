import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(8)
