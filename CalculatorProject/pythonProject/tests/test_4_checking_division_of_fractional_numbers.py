import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import CalculatorPage

@allure.description("test_4_checking_division_of_fractional_numbers")
def test_4_checking_division_of_fractional_numbers():
    """Проверка деления двух отрицательных чисел"""

    s = Service('C:\\Users\\vkil\\CalculatorProject\\pythonProject\\resources\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    print('Проверка деления дробных чисел')

    calculator = CalculatorPage(driver)
    calculator.checking_division_of_fractional_numbers()
    # time.sleep(3)

