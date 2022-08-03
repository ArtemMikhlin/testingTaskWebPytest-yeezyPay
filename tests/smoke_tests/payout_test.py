from pages_steps.payout_page_steps import PayoutPageSteps
from pages_steps.burger_menu_steps import BurgerMenuSteps
from pages_steps.history_page_steps import HistoryPageSteps
from pages_steps.main_page_steps import MainPageSteps
from base_methods import create_csv_file, get_last_transaction_data, update_authorization_link
import pytest


@pytest.mark.smoke
@pytest.mark.payout
@pytest.mark.parametrize(
    "card_number, status",
    [
        ({4111111111111111: 'accept_now', 'COMPLETE': 'status_complete'}),
        ({4444333322221111: 'decline_now',  'FAILED': 'status_failed'})
    ]
)
def test_payout_with_csv_file(browser, card_number, status, amount=1100, commission_percent=1,
                              fix_commission=40, currency="RUB", file="data/payout_files/payout_data_accept_now.csv"):
    browser.get(update_authorization_link()["authlink"])
    total_commission = round(amount * commission_percent / 100 + fix_commission)
    create_csv_file(card_number, amount, file)

    payout_page = PayoutPageSteps(browser)
    payout_page.check_payout_page_visible_after_authorization()

    # burger_menu = BurgerMenuSteps(browser)
    # burger_menu.open_main_menu()
    #
    # main_page = MainPageSteps(browser)
    # actual_account_balance = main_page.get_account_balance(currency)
    # burger_menu.open_payout_menu()

    payout_page.upload_file(file)
    payout_page.confirm_transaction(amount, commission_percent, total_commission)
    burger_menu = BurgerMenuSteps(browser)
    burger_menu.open_history_menu()

    history_page = HistoryPageSteps(browser)
    history_page.check_progressbar_status(status)

    last_transaction_data = get_last_transaction_data().json()['items'][0]
    assert last_transaction_data['status_name'] == status and \
           last_transaction_data['kind_name'] == 'WITHDRAW' and \
           round(last_transaction_data['amount']) == amount and \
           last_transaction_data['pan'] == str(card_number) and \
           round(last_transaction_data['fee']) == total_commission,  \
           f"'Transaction' isn't valid: Actual account data :{last_transaction_data['fee']}, " \
           f"{last_transaction_data['amount']}, {last_transaction_data['pan']},"

    # burger_menu.open_main_page()

    # actual_account_balance_after_transaction = round(main_page.get_account_balance(currency))
    # account_balance = round(actual_account_balance - amount + total_commission)

    # assert actual_account_balance_after_transaction == account_balance, \
    #     f"'Transaction' isn't valid: Actual account balance = {actual_account_balance_after_transaction}" \
    #     f", mast be = {account_balance}"
