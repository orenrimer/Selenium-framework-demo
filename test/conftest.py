import json
import logging
from settings import DIRS
from os.path import join
import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.utilities import custom_logger


@pytest.fixture(scope='session')
def config():
    config_path = join(DIRS['RESOURCES'], "config.json")
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def driver_setup(config):
    browser = config['BROWSER']
    driver_path = join(DIRS['TEST'], "resources", "drivers")
    logger = custom_logger

    if browser == "chrome":
        options = ChromeOptions()
        driver = Chrome(executable_path=join(driver_path, "chromedriver.exe"), options=options)
        logger.info("Opened new Chrome window")
    elif browser == "firefox":
        driver = Firefox(executable_path=join(driver_path, "geckodriver.exe"))
        logger.info("Opened Firefox window")
    else:
        raise Exception(f"Unsupported browser, can't open {browser}")

    driver.maximize_window()
    driver.get(config['BASE_URL'])
    logger.info(f"Go to URL:: {config['BASE_URL']}")
    driver.implicitly_wait(config['WAIT_TIME'])
    yield driver
    login_page = LoginPage(driver)
    cart = CartPage(driver)
    if login_page.verify_logged_in():
        cart.goto()
        if not cart.verify_empty_cart():
            cart.clear_cart()
        login_page.sign_out()
    driver.close()
