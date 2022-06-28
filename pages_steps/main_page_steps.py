from pages.main_page import MainPage
import allure


class MainPageSteps(MainPage):

    @allure.step("open_main_page")
    def open(self):
        self.open_main_page()
        self.check_main_page_visible()

    @allure.step("get_account_balance")
    def get_account_balance(self, currency):
        return self.get_main_account_balance(currency)
