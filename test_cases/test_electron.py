import allure
import pytest

from extensions.verifications import Verifications
from worksflow.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class TestElectron:

    @allure.title('Test01: Add and Verify New Task')
    @allure.description('This test adds a new task and verifies it in the list of tasks')
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task_flow('Learn Python')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks(), 1)

    @allure.title('Test01: Add and Verify New Tasks')
    @allure.description('This test adds new tasks and verifies it in the list of tasks')
    def test_add_and_verify_new_tasks(self):
        ElectronFlows.add_new_task_flow('Learn Java')
        ElectronFlows.add_new_task_flow('Learn JS')
        ElectronFlows.add_new_task_flow('Learn C#')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks(), 3)

    def teardown_method(self):
        ElectronFlows.empty_list()
