from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Belov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivan@mail.ru")
   
    file_button = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'Текстовый документ.txt')           # добавляем к этому пути имя файла 
    file_button.send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    print(file_path)
    time.sleep(10)
    browser.quit()