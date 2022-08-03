from base_methods import BaseMethods
from selenium.webdriver.common.by import By


class HistoryPage(BaseMethods):
    __PAGE_URL = "https://my.stage.yeezypay.io/history"

    __BUTTON_SEARCH = (By.CSS_SELECTOR, ".bi-search")

    __LABEL_DOWNLOAD = (By.CSS_SELECTOR, "[aria-label = 'cloud download fill']")

    __PROGRESSBAR_WAITING = (By.CSS_SELECTOR, ".bg-warning")

    __PROGRESSBAR_CANCEL = (By.CSS_SELECTOR, ".bg-danger")

    __PROGRESSBAR_COMPLETE = (By.CSS_SELECTOR, ".bg-success")

    def open_history_page(self):
        self.open_page(self.__PAGE_URL)

    def check_history_page_visible(self):
        assert self.wait_element_present(5, *self.__BUTTON_SEARCH) \
               or self.wait_element_present(5, *self.__LABEL_DOWNLOAD) is True, "'History' page isn't present!"

    def get_progressbar_status(self, status):
        if status == "WAITING":
            return self.wait_element_present(5, *self.__PROGRESSBAR_WAITING)

        elif status == "FAILED":
            return self.wait_element_present(5, *self.__PROGRESSBAR_CANCEL)

        elif status == "COMPLETE":
            return self.wait_element_present(5, *self.__PROGRESSBAR_COMPLETE)
