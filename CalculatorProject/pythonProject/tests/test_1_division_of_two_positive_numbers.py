import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import CalculatorPage

@allure.description("test_1_division_of_two_positive_numbers")
def test_1_division_of_two_positive_numbers():
    """Проверка деления двух положительных чисел"""

    s = Service('C:\\Users\\vkil\\CalculatorProject\\pythonProject\\resources\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    print('Проверка деления двух положительных чисел')

    calculator = CalculatorPage(driver)
    calculator.check_positive_division()
    # time.sleep(3)

    # print('Старт проверки деления двух отрицательных чисел')
    #
    # calculator = CalculatorPage(driver)
    # calculator.check_two_negative_numbers_division()
    #
    # print('Финиш')
    #
    # print('Старт проверки деления на ноль')
    #
    # calculator = CalculatorPage(driver)
    # calculator.checking_division_by_zero()
    # # time.sleep(3)
    #
    # print('Финиш')
    #
    # print('Старт проверки деления дробных чисел')
    #
    # calculator = CalculatorPage(driver)
    # calculator.checking_division_of_fractional_numbers()
    # # time.sleep(3)
    #
    # print('Финиш')
    #
    # print('Старт проверки деления положительного числа на отрицательное')
    #
    # calculator = CalculatorPage(driver)
    # calculator.checking_positive_number_divide_negative()
    # # time.sleep(3)
    #
    # print('Финиш')
















