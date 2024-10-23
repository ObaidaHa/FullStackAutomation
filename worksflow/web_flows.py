import time

import allure

import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from page_objects.web_objects.left_menu_page import server_admin, search
from page_objects.web_objects.server_admin_menu_page import users
from page_objects.web_objects.server_admin_page import users_list
from utilities.comon_ops import wait, For, get_data, read_csv


class WebFlows:
    @staticmethod
    @allure.step('Login To Grafana')
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_username(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    @allure.step('Verify Grafana Title flow')
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXIST, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    # verify menu buttons using smart assertions
    @staticmethod
    @allure.step('Verify menu buttons flow using smart assertion')
    def verify_menu_buttons_flow_smart_assertion():
        elems = [page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_settings(),
                 page.web_upper_menu.get_save(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)

    # verify menu buttons using my Implementation
    @staticmethod
    @allure.step('Verify menu buttons flow using my implementation')
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_settings(),
                 page.web_upper_menu.get_save(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_displayed(elems)

    # @staticmethod
    # def open_users():
    #     elem1 = page.web_left_menu.get_server_admin()
    #     elem2 = page.web_server_admin_menu.get_users()
    #     UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    @allure.step('Move to users flow')
    def open_users():
        wait(For.ELEMENT_DISPLAYED, server_admin)
        UiActions.click(page.web_left_menu.get_server_admin())

    @staticmethod
    @allure.step('create new user')
    def create_user(name, email, user, password):
        UiActions.click(page.web_server_admin.get_new_user())
        UiActions.update_text(page.web_server_admin_new_user.get_name(), name)
        UiActions.update_text(page.web_server_admin_new_user.get_email(), email)
        UiActions.update_text(page.web_server_admin_new_user.get_user_name(), user)
        UiActions.update_text(page.web_server_admin_new_user.get_password_new(), password)
        UiActions.click(page.web_server_admin_new_user.get_create_user())

    @staticmethod
    @allure.step('Verify number of users in table')
    def verify_number_of_users(number):
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.server_admin_page.users_list)
        if number > 0:
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(), number)

    @staticmethod
    @allure.step('search users table flow')
    def search_users(search_vlue):
        UiActions.clear(page.web_server_admin.get_search())
        UiActions.update_text(page.web_server_admin.get_search(), search_vlue)

    @staticmethod
    @allure.step('delete user from users table flow')
    def delete_user(by, value):
        if by == 'user':
            UiActions.click(page.web_server_admin.get_user_by_user_name(value))
        elif by == 'index':
            UiActions.click(page.web_server_admin.get_user_by_index(value))
        UiActions.click(page.web_server_admin.get_delete_user())
        UiActions.click(page.web_server_admin.get_confirm_delete())

    @staticmethod
    @allure.step('Go to Home flow')
    def grafana_home(self):
        self.driver.get(get_data('Url'))


data = read_csv(get_data('CSV_Location'))
testdata = [(data[0][0], data[0][1]),
            (data[1][0], data[1][1]),
            (data[2][0], data[2][1])]
