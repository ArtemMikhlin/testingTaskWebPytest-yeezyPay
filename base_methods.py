from decimal import Decimal

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import os
import re


def create_csv_file(card_number, amount, file_name):

    with open(file_name, "w") as file:
        file.write(f"{card_number};{amount};")


def get_num_from_string(string):
    return [float(s) for s in re.findall(r'\d*\.?\d+', string)]


class BaseMethods:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def click(self, *locator):
        element = self.browser.find_element(*locator)
        element.click()

    def input(self, value, *locator):
        element = self.browser.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def get_text_from_element(self, *locator):
        element = self.browser.find_element(*locator)
        return element.text

    def send_file(self, file, *locator):
        element = self.browser.find_element(*locator)
        current_dir = os.path.abspath(
            os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, file)  # добавляем к этому пути имя файла
        element.send_keys(file_path)

    def check_element_clickable(self, timeout, *locator):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False

        return True

    def check_text_from_element_is_visible(self, timeout, text, *locator):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False

        return True

    def check_element_invisible_without_waiting(self, *locator):
        try:
            EC.invisibility_of_element_located(locator)
        except TimeoutException:
            return False

        return True

    def wait_element_present(self, timeout, *locator):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True
