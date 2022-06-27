from base_methods import BaseMethods
from selenium.webdriver.common.by import By


class BurgerMenu(BaseMethods):
    __BUTTON_BURGER = (By.CSS_SELECTOR, "[aria-label = 'Toggle navigation']")
    __ITEM_MAIN = (By.CSS_SELECTOR, "[href = '/dashboard/']")
    __ITEM_HISTORY = (By.CSS_SELECTOR, "[href = '/history']")

    def click_on_burger_menu(self):
        self.click(*self.__BUTTON_BURGER)

    def click_on_item_history(self):
        self.click(*self.__ITEM_HISTORY)

    def click_on_item_main(self):
        self.click(*self.__ITEM_MAIN)

    def check_menu_is_opening(self):
        assert self.wait_element_present(10, *self.__ITEM_MAIN) \
               or self.wait_element_present(10, *self.__ITEM_HISTORY) is True, "'Burger' menu isn't present!"

