import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import CalculatorPage

@allure.description("test_3_checking_division_by_zero")
def test_3_checking_division_by_zero():
    """Проверка деления двух отрицательных чисел"""

    s = Service('C:\\Users\\vkil\\CalculatorProject\\pythonProject\\resources\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    print('Проверка деления на ноль')

    calculator = CalculatorPage(driver)
    calculator.checking_division_by_zero()
    # time.sleep(3)

