import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    @allure.step('verify equals two elements')
    def verify_equals(actual, expected):
        assert actual == expected, f'Verify Equals Failed, Actual: {actual} is not equals to expected: {expected}'

    @staticmethod
    @allure.step('Verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify is Displayed Failed, {elem.text} is not Displayed'

    @staticmethod
    @allure.step('Soft Verification (assert) of elements using smart-assertion')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()


    @staticmethod
    @allure.step('Soft verification (assert) of elements using my Implementation')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print(f'Soft Displayed Failed, Elements which failed: {failed_elem} is not displayed')
            raise AssertionError('Soft Displayed Failed')

    @staticmethod
    @allure.step('Verify number of elements in list')
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'Number of Elements is at least ' + str(
            len(elems)) + ', which does not match the expected size: ' + str(size)
