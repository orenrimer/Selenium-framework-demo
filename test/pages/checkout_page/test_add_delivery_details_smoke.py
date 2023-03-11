from os.path import join
import pytest
import unittest
from ddt import ddt, data, unpack
from settings import DIRS
from src.pages.cart_page import CartPage
from src.pages.checkout_pages.delivery_page import DeliveryPage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.results_page import ResultsPage
from src.utilities.read_data import getCSVData

pytestmark = [pytest.mark.smoke, pytest.mark.checkout, pytest.mark.deliverypage]


@ddt
class TestAddDeliveryAddress(unittest.TestCase):
    data_path = join(DIRS['RESOURCES'], "test_data", "AddressRecords.csv")

    @pytest.fixture()
    def setup(self, driver_setup):
        self.login_page = LoginPage(driver_setup)
        self.results_page = ResultsPage(driver_setup)
        self.product_page = ProductPage(driver_setup)
        self.cart = CartPage(driver_setup)
        self.delivery_page = DeliveryPage(driver_setup)
        self.product = "jeans"

    @pytest.fixture()
    def preconditions(self, setup):
        if not self.login_page.verify_logged_in():
            self.login_page.goto()
            self.login_page.login()
        self.results_page.goto_product(self.product)
        self.product_page.add_to_bag(select_type="dropdown")
        self.cart.goto()
        self.cart.goto_checkout_page()
        yield
        self.delivery_page.go_back_to_home_page()

    @pytest.mark.tcid25
    @data(*getCSVData(data_path))
    @unpack
    @pytest.mark.usefixtures("setup", "preconditions")
    def test_add_valid_delivery_details(self, fullAddress, Postcode, PhoneNum):
        self.delivery_page.enter_full_delivery_details(phone=PhoneNum, postcode=Postcode, full_address=fullAddress)
        assert self.delivery_page.verify_valid_delivery_details()
        if AssertionError:
            self.delivery_page.driver.take_screenshot(name="test_add_valid_delivery_details")
