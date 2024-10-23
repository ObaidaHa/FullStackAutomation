import allure
from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class DesktopFlows:
    @staticmethod
    @allure.step('Calculate equation')
    def calculate_flow(equation):
        for i in equation:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_calc.get_equals())

    @staticmethod
    def calculator_click(value):
        actions = {
            '0': page.standard_calc.get_zero,
            '1': page.standard_calc.get_one,
            '2': page.standard_calc.get_two,
            '3': page.standard_calc.get_three,
            '4': page.standard_calc.get_four,
            '5': page.standard_calc.get_five,
            '6': page.standard_calc.get_six,
            '7': page.standard_calc.get_seven,
            '8': page.standard_calc.get_eight,
            '9': page.standard_calc.get_nine,
            '/': page.standard_calc.get_divide,
            '*': page.standard_calc.get_multiple,
            '+': page.standard_calc.get_add,
            '-': page.standard_calc.get_minus
        }
        if value in actions:
            UiActions.click(actions[value]())
        else:
            raise Exception(f"Invalid Input: {value}")

    @staticmethod
    @allure.step('Get calculator result')
    def get_result_flow():
        result = page.standard_calc.get_result().text.replace("Display is", "").strip()
        return result

    @staticmethod
    @allure.step('Clear calculator page')
    def clear_flow():
        UiActions.click(page.standard_calc.get_clear())
