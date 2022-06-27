from pages.main_page import MainPage


class MainPageSteps(MainPage):
    def open(self):
        self.open_main_page()
        self.check_main_page_visible()

    def get_account_balance(self, currency):
        return self.get_main_account_balance(currency)
