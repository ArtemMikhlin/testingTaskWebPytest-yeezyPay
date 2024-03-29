from pages_steps.payout_page_steps import PayoutPageSteps
from pages_steps.burger_menu_steps import BurgerMenuSteps
from pages_steps.main_page_steps import MainPageSteps
from base_methods import create_csv_file, update_authorization_link
import pytest


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.payout
@pytest.mark.parametrize(
    "card_number, amount",
    [
        ({4111111111111111: 'valid_card_number', 0: 'invalid_amount'}),
        ({0: 'invalid_card_number', 100: 'valid_amount'})
    ]
)
def test_payout_with_invalid_csv_file_data(browser, card_number, amount, currency="RUB",
                                           file="data/payout_files/payout_data_invalid_data.csv", ):
    browser.get(update_authorization_link()["authlink"])
    create_csv_file(card_number, amount, file)

    payout_page = PayoutPageSteps(browser)
    payout_page.check_payout_page_visible_after_authorization()

    burger_menu = BurgerMenuSteps(browser)
    # burger_menu.open_main_menu()

    # main_page = MainPageSteps(browser)
    # actual_account_balance = main_page.get_account_balance(currency)
    burger_menu.open_payout_menu()

    payout_page.upload_file(file)
    payout_page.cancel_transaction_with_invalid_data()
    # burger_menu.open_main_menu()
    # actual_account_balance_after_canceled_transaction = main_page.get_account_balance(currency)

    # assert actual_account_balance == actual_account_balance_after_canceled_transaction, \
    #     f"Balance after canceled transaction is changed!Before :{actual_account_balance}," \
    #     f" After {actual_account_balance_after_canceled_transaction}"
