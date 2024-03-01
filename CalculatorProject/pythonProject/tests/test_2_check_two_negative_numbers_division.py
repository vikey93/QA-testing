import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import CalculatorPage

@allure.description("test_2_check_two_negative_numbers_division")
def test_2_check_two_negative_numbers_division():
    """Проверка деления двух отрицательных чисел"""

    s = Service('C:\\Users\\vkil\\CalculatorProject\\pythonProject\\resources\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    print('Проверка деления двух отрицательных чисел')

    calculator = CalculatorPage(driver)
    calculator.check_two_negative_numbers_division()

