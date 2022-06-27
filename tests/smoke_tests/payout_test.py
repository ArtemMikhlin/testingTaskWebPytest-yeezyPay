from pages_steps.payout_page_steps import PayoutPageSteps
from pages_steps.burger_menu_steps import BurgerMenuSteps
from pages_steps.history_page_steps import HistoryPageSteps
from pages_steps.main_page_steps import MainPageSteps
from base_methods import create_csv_file
import pytest


@pytest.mark.smoke
@pytest.mark.payout
def test_payout_with_csv_file(browser, card_number=4111111111111111, amount=1100, commission_percent=1,
                              fix_commission=40, currency="RUB", file="data/payout_files/payout_data_accept_now.csv",
                              status="Complete"):
    total_commission = round(amount * commission_percent / 100 + fix_commission)
    create_csv_file(card_number, amount, file)

    burger_menu = BurgerMenuSteps(browser)
    burger_menu.open_main_menu_item()

    main_page = MainPageSteps(browser)
    actual_account_balance = main_page.get_account_balance(currency)

    payout_page = PayoutPageSteps(browser)
    payout_page.open()
    payout_page.upload_file(file)
    payout_page.confirm_transaction(amount, commission_percent, total_commission)
    burger_menu = BurgerMenuSteps(browser)
    burger_menu.open_history_menu_item()

    history_page = HistoryPageSteps(browser)
    history_page.check_progressbar_status(status)
    burger_menu.open_main_page()

    actual_account_balance_after_transaction = round(main_page.get_account_balance(currency))
    account_balance = round(actual_account_balance - amount + total_commission)

    assert actual_account_balance_after_transaction == account_balance, \
        f"'Transaction' isn't valid: Actual account balance = {actual_account_balance_after_transaction}" \
        f", mast be = {account_balance}"
