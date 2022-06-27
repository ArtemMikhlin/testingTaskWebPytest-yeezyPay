from pages.history_page import HistoryPage


class HistoryPageSteps(HistoryPage):

    def open(self):
        self.open_history_page()
        self.check_history_page_visible()

    def check_progressbar_status(self, status):
        assert self.get_progressbar_status(status) is True, f"'{status}' progressbar isn't present!"
