import allure
import pytest

from worksflow.db_flows import DBFlows
from worksflow.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_Web_DB:
    @allure.title('Test01: Login to Grafana via DB')
    @allure.description('This test verify login using elements taken from database')
    def test_verify_login_db(self):
        DBFlows.login_grafana_via_db()
        WebFlows.verify_grafana_title('Welcome to Grafana')