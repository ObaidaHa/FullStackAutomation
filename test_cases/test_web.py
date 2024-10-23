import allure
import pytest

from utilities.comon_ops import get_data, By
from worksflow import web_flows
from worksflow.web_flows import WebFlows
import test_cases.conftest as conf


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:

    @allure.title('Test 01: Verify Login Grafana')
    @allure.description('This test verifies a successful login to Grafana')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebFlows.verify_grafana_title('Welcome to Grafana')

    @allure.title('Test 02: Verify Upper Menu Buttons')
    @allure.description('This test verifies the upper menu buttons')
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertion()  # smart-assertions
        # WebFlows.verify_menu_buttons_flow()               # My_Implementation

    @allure.title('Test 03: Verify Creating New Users')
    @allure.description('This test creating and verifies new users')
    def test_verify_new_user(self):
        WebFlows.open_users()
        WebFlows.create_user('Obaida', 'handoklu@gmail.com', 'Obaidah', 'h12345')
        WebFlows.create_user('Tariq', 'tarig@gmail.com', 'Tariqg', 't12345')
        WebFlows.verify_number_of_users(3)

    @allure.title('Test 04: Filtering Users')
    @allure.description('This test verifies filtering users')
    @pytest.mark.parametrize('search_vlue,expected_users', web_flows.testdata)
    def test_filter_by_user_name(self, search_vlue, expected_users):
        WebFlows.open_users()
        WebFlows.search_users(search_vlue)
        WebFlows.verify_number_of_users(int(expected_users))

    @allure.title('Test 05: Delete Users')
    @allure.description('This test verifies deleted users')
    def test_verify_deleted_user(self):
        WebFlows.open_users()
        WebFlows.delete_user(By.USER, 'Obaidah')  # Option 1
        WebFlows.delete_user(By.INDEX, 0)  # Option 2
        WebFlows.verify_number_of_users(1)

    # @allure.title('Test 06: Visual Testing')
    # @allure.description('This tet verifies visually users table')
    # @pytest.mark.skipif(get_data('ExecuteApplitools').lower() == 'no', reason='run this test on selenium 3.141.0 & appium 3.2.1')
    # def test_visual_verify_deleted_user(self):
    #     conf.eyes.open(self.driver, 'Grafana', 'Grafana testing user table')
    #     WebFlows.login_flow(get_data('UserName'), get_data('Password'))
    #     conf.driver.get('http://localhost:3000/admin/users')
    #     conf.eyes.check_window('Users Table')

    def teardown_method(self):
        WebFlows.grafana_home(self)
