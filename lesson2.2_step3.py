from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    numero1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = numero1.text
    numero2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = numero2.text
    sum = int(num1) + int(num2)
    string = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    answer = select.select_by_value(string)

    browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(5)
    browser.quit()