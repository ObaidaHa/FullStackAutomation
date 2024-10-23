import time

import allure
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page

from extensions.ui_actions import UiActions


class ElectronFlows:
    @staticmethod
    @allure.step('Add new task flow')
    def add_new_task_flow(task_name):
        UiActions.update_text(page.electron_task.get_create(), task_name)
        UiActions.update_text(page.electron_task.get_create(), Keys.RETURN)

    @staticmethod
    @allure.step('Get number of tasks')
    def get_number_of_tasks():
        return len(page.electron_task.get_tasks())

    @staticmethod
    @allure.step('Empty task from list')
    def empty_list():
        for x in range(ElectronFlows.get_number_of_tasks()):
            time.sleep(0.5)
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])
