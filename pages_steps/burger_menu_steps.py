from pages.burger_menu import BurgerMenu
from pages.main_page import MainPage
from pages.history_page import HistoryPage


class BurgerMenuSteps(BurgerMenu, MainPage, HistoryPage):

    def open(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()

    def open_history_menu_item(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()
        self.click_on_item_history()
        self.check_history_page_visible()

    def open_main_menu_item(self):
        self.click_on_burger_menu()
        self.check_menu_is_opening()
        self.click_on_item_main()
        self.check_main_page_visible()
