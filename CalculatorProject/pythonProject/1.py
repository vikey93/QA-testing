from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=калькулятор')

# Находим поле ввода и вводим математическое выражение
six_btn = driver.find_element(By.XPATH, "//div[@jsname='abcgof']")
six_btn.click()
divide_btn = driver.find_element(By.XPATH, "//div[@jsname='WxTTNd']")
divide_btn.click()
two_btn = driver.find_element(By.XPATH, "//div[@jsname='lVjWed']")
two_btn.click()
equals_btn = driver.find_element(By.XPATH, "//div[@jsname='Pt8tGc']")
equals_btn.click()
time.sleep(2)
sum_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='cwos']")))
print(sum_field.text)
time.sleep(2)

# # Находим результат вычисления и сохраняем его в переменную
# result = driver.find_element_by_id('cwos')
# print(result.text)

# Закрываем браузер
driver.quit()