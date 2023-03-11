import json
import logging
from settings import DIRS
from os.path import join
import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.utilities import custom_logger


logger = custom_logger
BASE_URL = "https://www.topman.com/"


@pytest.fixture(scope='session')
def config():
    config_path = join(DIRS['RESOURCES'], "config.json")
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def driver_setup(config):
    browser = config['BROWSER']

    if browser == "chrome":
        driver_path = join(DIRS['TEST'], "resources", "drivers", "chromedriver.exe")
        logging.info(driver_path)
        options = ChromeOptions()
        driver = Chrome(executable_path=driver_path, options=options)
        logger.info("Opened Chrome window")
    elif browser == "firefox":
        driver = Firefox()
        logger.info("Opened Firefox window")
    else:
        raise Exception(f"Unsupported browser, can't open {browser}")
        
    driver.maximize_window()
    driver.get(BASE_URL)
    logger.info(f"Go to URL:: {BASE_URL}")
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
