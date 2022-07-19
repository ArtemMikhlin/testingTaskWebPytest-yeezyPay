import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture(scope="function")
def browser(auth_url="https://my.stage.yeezypay.io/auth/WzI3LCAiYjh0NDdhLTZjNTNlYTYzZTEzZDk2N2FjODk0ZGNlZTQzNTM1MTRjIl0="):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # driver install, post options
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(5)
    browser.get(auth_url)
    print("\nstart browser for test..")
    yield browser
    browser.quit()
    print("\nbrowser close")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            allure.attach(
                item.funcargs['browser'].get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
