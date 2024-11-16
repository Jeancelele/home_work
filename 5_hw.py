from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements_on_page():
    # Настройки веб-драйвера
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    # Поиск элементов
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn_action')

    if username_field and password_field and submit_button:
        print("Элементы найдены")

    driver.quit()  # Закрываем браузер

# Вызов функции
check_elements_on_page()
