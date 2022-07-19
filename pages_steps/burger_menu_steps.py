from pages.burger_menu import BurgerMenu
from pages.main_page import MainPage
from pages.history_page import HistoryPage
from pages.payout_page import PayoutPage
from pages.exchange_page import ExchangePage
import allure


class BurgerMenuSteps(BurgerMenu, MainPage, HistoryPage, PayoutPage, ExchangePage):

    @allure.step("open_burger_menu")
    def open(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()

    @allure.step("open_history_menu_item")
    def open_history_menu(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()
        self.click_on_item_history()
        self.check_history_page_visible()

    # @allure.step("open_main_menu_item")
    # def open_main_menu(self):
    #     self.click_on_burger_menu()
    #     self.check_menu_is_opening()
    #     self.click_on_item_main()
    #     self.check_main_page_visible()

    @allure.step("open_payout_menu_item")
    def open_payout_menu(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()
        self.click_on_item_payout()
        self.check_payout_page_visible()

    @allure.step("open_exchange_menu_item")
    def open_exchange_menu(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()
        self.click_on_item_exchange()
        self.check_exchange_page_visible()
