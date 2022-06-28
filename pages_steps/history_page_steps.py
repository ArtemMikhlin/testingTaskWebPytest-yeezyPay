from pages.history_page import HistoryPage
import allure


class HistoryPageSteps(HistoryPage):

    @allure.step("open_history_page")
    def open(self):
        self.open_history_page()
        self.check_history_page_visible()

    @allure.step("check_progressbar_status")
    def check_progressbar_status(self, status):
        assert self.get_progressbar_status(status) is True, f"'{status}' progressbar isn't present!"
