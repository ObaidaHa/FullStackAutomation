import allure

import test_cases.conftest as conf
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.comon_ops import get_data


class MobileFlows:
    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, save):
        MobileActions.update_text(page.mobile_calculator.get_amount(), amount)
        MobileActions.update_text(page.mobile_calculator.get_term(), term)
        MobileActions.update_text(page.mobile_calculator.get_rate(), rate)
        MobileActions.click(page.mobile_calculator.get_calculate())
        if save:
            MobileActions.click(page.mobile_calculator.get_save())

    @staticmethod
    @allure.step('Verify repayment flow')
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        Verifications.verify_equals(actual, '£' + expected)

    @staticmethod
    @allure.step('Swipe to save screen')
    def swipe_screen(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']

        start_x = None
        start_y = None
        end_x = None
        end_y = None

        if direction == 'left':
            start_x = width * 0.8
            end_x = width * 0.2
            start_y = end_y = height * 0.2
        if direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5
        if direction == 'up':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5
        if direction == 'down':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5
        MobileActions.swipe(start_x, start_y, end_x, end_y, int(get_data('SwipeDuration')))

    @staticmethod
    @allure.step('Verify and delete saved transactions flow')
    def verify_saved_delete_transaction(expected_amount, expected_term, expected_rate):
        actual_amount = page.mobile_saved.get_amount().text
        actual_term = page.mobile_saved.get_term().text
        actual_rate = page.mobile_saved.get_rate().text
        Verifications.verify_equals(actual_amount, '£' + expected_amount)
        Verifications.verify_equals(actual_term, 'yrs' + expected_term)
        Verifications.verify_equals(actual_rate, expected_rate + '%')
        MobileActions.tap(page.mobile_saved.get_delete(), 1)
        MobileActions.tap(page.mobile_saved.get_confirm_delete(), 1)
