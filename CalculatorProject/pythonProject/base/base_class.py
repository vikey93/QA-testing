from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Callable, Optional

from selenium.webdriver.remote.webelement import WebElement




class ExceptionWebElementNotFound(Exception):
    def __init__(self, by: str, selector: str):
        super().__init__(f"Невозможно найти WebElement по {by} == <{selector}>")


class Base():
    driver: WebDriver

    description: str = "Базовый класс страницы"

    url: str = 'https://www.google.com/search?q=калькулятор'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Сумма = ', result)

    # def get_web_element(self, by: str, selector: str):
    #     """Method get web element"""
    #     try:
    #         return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((by.)))
    #     except Exception as e:
    #         raise ExceptionWebElementNotFound(by, selector)

    # def assert_word(self,
    #                 word_element_getter: Callable[[], WebElement],
    #                 result: str,
    #                 *,
    #                 property_name: Optional[str] = None
    #                 ):
    #     """Method assert value"""
    #     element = word_element_getter()
    #     if property_name is None:
    #         value_word = element.text
    #     else:
    #         value_word = element.get_property(property_name)
    #     assert value_word == result, f"<{value_word}> must be equal <{result}>"
    #     print('Correct value! =', result)



