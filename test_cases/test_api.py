import allure

from extensions.verifications import Verifications
from worksflow.api_flows import APIFlows

team_name = 'obaida'
team_email = 'obaida@gmail.com'


class TestAPI:
    @allure.title('Test01: Create team & Verify Status Code')
    @allure.description('This test creates new team in Grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test02: Verify Team Name')
    @allure.description('This test verifies the Grafana team member name')
    def test_verify_team_member_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.title('Test03: Update Team & Verify Status Code')
    @allure.description('This test update team and verify status code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + ' Handoklu', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Verify Team Name')
    @allure.description('This test verifies the Grafana team member name after updates')
    def test_verify_updated_team_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name + ' Handoklu')

    @allure.title('Test05: Delete Team & Verify Status Code')
    @allure.description('This test delete team and verifies status code')
    def test_delete_team_and_verify(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)


