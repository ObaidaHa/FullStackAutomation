from selenium.webdriver.common.by import By

amount = (By.ID, "etAmount")
term = (By.ID, "etTerm")
rate = (By.ID, "etRate")
calculate = (By.ID, "btnCalculate")
save = (By.ID, "btnSave")
repayment = (By.ID, "tvRepayment")
interest = (By.ID, "tvInterestOnly")


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(amount[0], amount[1])

    def get_term(self):
        return self.driver.find_element(term[0], term[1])

    def get_rate(self):
        return self.driver.find_element(rate[0], rate[1])

    def get_calculate(self):
        return self.driver.find_element(calculate[0], calculate[1])

    def get_save(self):
        return self.driver.find_element(save[0], save[1])

    def get_repayment(self):
        return self.driver.find_element(repayment[0], repayment[1])

    def get_interest(self):
        return self.driver.find_element(interest[0], interest[1])
