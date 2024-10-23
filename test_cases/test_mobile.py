import allure
import pytest

from utilities.comon_ops import Save, Direction
from worksflow.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:
    @allure.title('Test01: Verify Mortgage Repayment')
    @allure.description('this test verifies the mortgage repayment')
    def test_verify_repayment(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.NO)
        MobileFlows.verify_mortgage_repayment('17.94')

    @allure.title('Test02: Verify Save Details')
    @allure.description('this test verifies save transaction details')
    def test_saved_details(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.YES)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_saved_delete_transaction('1000', '5.0', '3.0')
