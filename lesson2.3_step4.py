from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[class='container'] [type='submit']")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm_text = confirm.text
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    time.sleep(10)
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
          
    link_stepik_lesson = "https://stepik.org/lesson/184253/step/4?unit=158843"
    browser = webdriver.Chrome()
    browser.get(link_stepik_lesson)
    time.sleep(10)
    
    sign_in_button = browser.find_element(By.CSS_SELECTOR, '[href="/course/575/promo?auth=login"]')
    sign_in_button.click()
    time.sleep(3)
    login_input = browser.find_element(By.ID, "id_login_email")
    login_input.send_keys("smoukus@mail.ru")
    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys("96357415n")
    sign_in_button2 = browser.find_element(By.CSS_SELECTOR, "[id='login_form'] button[type='submit']")
    sign_in_button2.click()
    time.sleep(10)

    lesson_link = browser.find_element(By.CSS_SELECTOR, '[class="lesson-widget__title"] [href="/lesson/184253/step/1?unit=158843"]')
    lesson_link.click()
    time.sleep(10)

    lesson_icon = browser.find_element(By.CSS_SELECTOR, "[class='html-content rich-text-viewer ember-view'] [href='/lesson/184253/step/4']")
    lesson_icon.click()            
    time.sleep(10)

    field = browser.find_element(By.TAG_NAME, 'textarea')
    field.send_keys(addToClipBoard)
    stepik_submit_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    stepik_submit_button.click()

finally:
    time.sleep(10)
    browser.quit()