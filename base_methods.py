import requests
import urllib3

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import os
import re
import allure
import requests
import urllib3
import hmac
import hashlib
import logging


@allure.step("create_csv_file")
def create_csv_file(card_number, amount, file_name):
    with open(file_name, "w") as file:
        file.write(f"{card_number};{amount};")


def get_num_from_string(string):
    return [float(s) for s in re.findall(r'\d*\.?\d+', string)]


def get_last_transaction_data():
    session = requests.Session()
    urllib3.disable_warnings()
    cookies = {'sessionid': '7s6sdjdjlhgzfis0d7paj6abyn4tiflf',
               'csrftoken': 'PMZnMcKPiw8cattTdqTM7ilDH7rPDWqeGu1BpY7JdZCADtRa3NIc56zCSUJf2nXl'}
    payout_headers = {'Content-type': 'application/x-www-form-urlencoded'}
    return session.get('https://my.stage.yeezypay.io/api/client/finance/payouts/', headers=payout_headers,
                       cookies=cookies)


def sign(data):
    logger = logging.getLogger(__name__)
    key = "Oshe[yieVai?ghuGee}cieng7aghae0K"
    msg = "\n".join(f"{k}={v or ''}" for k, v in sorted(data.items()))
    logger.info(f'sign msg: "{msg}" with key "{key}"')
    hkey = hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()
    return hkey


@allure.step("pdate_authorization_link")
def update_authorization_link():
    urllib3.disable_warnings()
    authorization_headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {'user_id': 470962052, 'hash': sign({"user_id": 470962052})}
    response_authorization = (requests.post('https://my.stage.yeezypay.io/api/telegram/get/authlink/',
                                                 verify=False, headers=authorization_headers, data=data))
    return response_authorization.json()


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
