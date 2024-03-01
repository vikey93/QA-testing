import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import CalculatorPage

@allure.description("test_5_checking_positive_number_divide_negative")
def test_5_checking_positive_number_divide_negative():
    """Проверка деления двух отрицательных чисел"""

    s = Service('C:\\Users\\vkil\\CalculatorProject\\pythonProject\\resources\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    print('Проверки деления положительного числа на отрицательное')

    calculator = CalculatorPage(driver)
    calculator.checking_positive_number_divide_negative()
    # time.sleep(3)








