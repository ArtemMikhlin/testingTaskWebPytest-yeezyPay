from pages.payout_page import PayoutPage
import allure


class PayoutPageSteps(PayoutPage):

    @allure.step("open_payout_page")
    def open(self):
        self.open_payout_page()
        self.check_payout_page_visible()

    @allure.step("check_payout_page_visible_after_authorization")
    def check_payout_page_visible_after_authorization(self):
        self.check_payout_page_visible()

    @allure.step("upload_file")
    def upload_file(self, file=str):
        self.click_on_button_upload_file()
        self.check_upload_file_section_visible()
        self.click_on_button_choose_file(file)
        self.click_on_button_send_funds()

    @allure.step("confirm_transaction")
    def confirm_transaction(self, total_amount=int, commission_percent=int, total_commission=int):
        self.check_pop_up_visible()
        self.check_data_from_pop_up(total_amount, commission_percent, total_commission)
        self.click_on_button_confirm()

    @allure.step("cancel_transaction_with_invalid_data")
    def cancel_transaction_with_invalid_data(self):
        self.check_pop_up_visible()
        self.check_button_confirm_invisible()
        self.click_on_button_cancel()
        self.click_on_button_yes()
