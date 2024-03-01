from base.base_class import Base
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure




class CalculatorPage(Base):
    """Страница с калькулятором"""
    description: str = "Страница калькулятор Google"

    url: str = 'https://www.google.com/search?q=калькулятор'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    six_btn = "//div[@jsname='abcgof']"
    divide_btn = "//div[@jsname='WxTTNd']"
    two_btn = "//div[@jsname='lVjWed']"
    equals_btn = "//div[@jsname='Pt8tGc']"
    sum_field = "//*[@id='cwos']"
    minus_btn = "//div[@jsname='pPHzQc']"
    calc_input = "//div[@jsname='VssY5c']"
    clear_btn = "//div[@jsname='SLn8gc']"
    one_btn = "//div[@jsname='N10B9']"
    zero_btn = "//div[@jsname='bkEvMb']"
    five_btn = "//div[@jsname='Ax5wH']"
    dot_btn = "//div[@jsname='YrdHyf']"


    # Getters

    def get_six_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.six_btn)))

    def get_divide_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.divide_btn)))

    def get_two_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.two_btn)))

    def get_equals_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.equals_btn)))

    def get_sum_field(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sum_field)))

    def get_minus_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.minus_btn)))

    def get_clear_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.clear_btn)))

    def get_one_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.one_btn)))

    def get_zero_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.zero_btn)))

    def get_five_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.five_btn)))

    def get_dot_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.dot_btn)))


    # Actions
    def click_six_button(self):
        self.get_six_btn().click()
        print('6')

    def click_divide_button(self):
        self.get_divide_btn().click()
        print('/')

    def click_two_button(self):
        self.get_two_btn().click()
        print('2')

    def click_equals_button(self):
        self.get_equals_btn().click()
        print('=')

    def click_minus_button(self):
        self.get_minus_btn().click()
        print('-')

    def click_clear_button(self):
        self.get_clear_btn().click()
        print('AC')

    def click_one_button(self):
        self.get_one_btn().click()
        print('1')

    def click_zero_button(self):
        self.get_zero_btn().click()
        print('0')

    def click_five_button(self):
        self.get_five_btn().click()
        print('5')

    def click_dot_button(self):
        self.get_dot_btn().click()
        print('.')




    def check_positive_division(self):
        with allure.step("check_positive_division"):
            self.driver.get(self.url)
            self.click_six_button()
            self.click_divide_button()
            self.click_two_button()
            self.click_equals_button()
            self.assert_word(self.get_sum_field(), '3')

    def check_two_negative_numbers_division(self):
        with allure.step("check_two_negative_numbers_division"):
            self.driver.get(self.url)
            self.click_minus_button()
            self.click_one_button()
            self.click_zero_button()
            self.click_divide_button()
            self.click_minus_button()
            self.click_two_button()
            self.click_equals_button()
            self.assert_word(self.get_sum_field(), '5')

    def checking_division_by_zero(self):
        with allure.step("checking_division_by_zero"):
            self.driver.get(self.url)
            self.click_two_button()
            self.click_divide_button()
            self.click_zero_button()
            self.click_equals_button()
            self.assert_word(self.get_sum_field(), 'Infinity')

    def checking_division_of_fractional_numbers(self):
        with allure.step("checking_division_of_fractional_numbers"):
            self.driver.get(self.url)
            self.click_one_button()
            self.click_dot_button()
            self.click_five_button()
            self.click_divide_button()
            self.click_zero_button()
            self.click_dot_button()
            self.click_five_button()
            self.click_equals_button()
            self.assert_word(self.get_sum_field(), '3')

    def checking_positive_number_divide_negative(self):
        with allure.step("checking_division_of_fractional_numbers"):
            self.driver.get(self.url)
            self.click_six_button()
            self.click_divide_button()
            self.click_minus_button()
            self.click_two_button()
            self.click_equals_button()
            self.assert_word(self.get_sum_field(), '-3')


























