from base_methods import *
from selenium.webdriver.common.by import By


class MainPage(BaseMethods):
    __PAGE_URL = "https://my.stage.yeezypay.io/dashboard/"

    __TABLE_TRANSACTION = (By.CSS_SELECTOR, ".table-responsive")

    __TEXT_MAIN_ACCOUNT_BALANCE = (By.CSS_SELECTOR, ".text-muted")

    def open_main_page(self):
        self.open_page(self.__PAGE_URL)

    def check_main_page_visible(self):
        assert self.wait_element_present(10, *self.__TABLE_TRANSACTION) \
               or self.wait_element_present(10, *self.__TEXT_MAIN_ACCOUNT_BALANCE) is True, "'Main' page isn't present!"

    def get_main_account_balance(self, currency):
        assert self.check_text_from_element_is_visible(3, currency, *self.__TEXT_MAIN_ACCOUNT_BALANCE) \
               is True, "'Account balance' isn't present!"
        account_balance_text = self.get_text_from_element(*self.__TEXT_MAIN_ACCOUNT_BALANCE)
        return get_num_from_string(account_balance_text)[0]
