from base_methods import BaseMethods
from selenium.webdriver.common.by import By


class PayoutPage(BaseMethods):
    __PAGE_URL = "https://my.stage.yeezypay.io/payout"

    __BUTTON_UPLOAD_FILE = (By.CSS_SELECTOR, "[aria-label='upload']")

    __BUTTON_SEND_FUNDS = (By.CSS_SELECTOR, "[aria-label='cursor fill']")

    # Section upload file
    __BUTTON_CHOOSE_FILE = (By.CSS_SELECTOR, ".form-control-file")

    # Pop - Up Confirm transaction
    __BUTTON_CONFIRM = (By.CSS_SELECTOR, ".btn-success")

    __BUTTON_CANCEL = (By.CSS_SELECTOR, ".modal-footer .btn-secondary")

    __TEXT_FIRST_CARD_NUMBER = (By.CSS_SELECTOR, ".text-center div:nth-child(2)")

    __TEXT_FIRST_AMOUNT = (By.CSS_SELECTOR, ".text-center div:nth-child(2)")

    __TEXT_TOTAL_AMOUNT = (By.CSS_SELECTOR, ".text-center:last-child div:nth-child(2)")

    __TEXT_COMMISSION = (By.CSS_SELECTOR, ".text-center:last-child div:last-child")

    # Pop - Up Payment in processing
    __BUTTON_CREATE_NEW_PAYMENT = (By.CSS_SELECTOR, ".modal-footer .btn-secondary")

    # Pop - Up Payment canceled
    __BUTTON_YES = (By.CSS_SELECTOR, ".modal-footer:nth-child(2) .btn-secondary:nth-child(1)")

    def open_payout_page(self):
        self.open_page(self.__PAGE_URL)

    def check_payout_page_visible(self):
        assert self.wait_element_present(5, *self.__BUTTON_UPLOAD_FILE) \
               or self.wait_element_present(5,
                                            *self.__BUTTON_SEND_FUNDS) is True, "'Payout' page isn't present!"

    def click_on_button_upload_file(self):
        assert self.check_element_clickable(5, *self.__BUTTON_UPLOAD_FILE) is True, \
            "'Upload' button isn't clickable!"
        self.click(*self.__BUTTON_UPLOAD_FILE)

    def click_on_button_send_funds(self):
        assert self.check_element_clickable(5, *self.__BUTTON_SEND_FUNDS) is True, \
            "'Send Funds' button isn't clickable!"
        self.click(*self.__BUTTON_SEND_FUNDS)

    # Upload file section
    def check_upload_file_section_visible(self):
        assert self.wait_element_present(5, *self.__BUTTON_CHOOSE_FILE) \
               or self.wait_element_present(5, *self.__BUTTON_SEND_FUNDS) is True, \
               "'Upload file' section isn't present!"

    def click_on_button_choose_file(self, file):
        self.send_file(file, *self.__BUTTON_CHOOSE_FILE)

    # Pop - Up Confirm transaction

    def check_pop_up_visible(self):
        assert self.wait_element_present(5, *self.__TEXT_TOTAL_AMOUNT) \
               or self.wait_element_present(5,
               *self.__TEXT_COMMISSION) is True, "'Confirm transaction' pop-up isn't present!"

    def click_on_button_confirm(self):
        self.click(*self.__BUTTON_CONFIRM)

    def click_on_button_cancel(self):
        self.click(*self.__BUTTON_CANCEL)

    def check_button_confirm_invisible(self):
        assert self.check_element_invisible_without_waiting(*self.__BUTTON_CONFIRM) is True,\
            "'Confirm' button isn present!"

    def check_data_from_pop_up(self, total_amount, commission_percent, total_commission):
        assert self.check_text_from_element_is_visible(3, f" {str(total_amount)} ", *self.__TEXT_TOTAL_AMOUNT) \
               is True, "'Total amount' isn't write!"
        assert self.check_text_from_element_is_visible(3, f"({str(commission_percent)}%): {total_commission} ",
                                                       *self.__TEXT_COMMISSION) is True, "'Commission' isn't write!"

    # Pop - Up Payment in processing
    def click_on_button_create_new_payment(self):
        assert self.check_element_clickable(10, *self.__BUTTON_CREATE_NEW_PAYMENT) is True, \
            "'Create new payment' button isn't clickable!"
        self.click(*self.__BUTTON_CREATE_NEW_PAYMENT)

    # Pop - Up Payment canceled
    def click_on_button_yes(self):
        assert self.check_element_clickable(10, *self.__BUTTON_YES) is True, \
            "'Yes' button isn't clickable!"
        self.click(*self.__BUTTON_YES)
