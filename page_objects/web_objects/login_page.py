from selenium.webdriver.common.by import By

user_name = (By.CSS_SELECTOR, "input[aria-label='Username input field']")
password = (By.CSS_SELECTOR, "input[aria-label='Password input field']")
submit = (By.CSS_SELECTOR, "button[aria-label='Login button']")
skip = (By.CSS_SELECTOR, "button[aria-label='Skip change password button']")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_submit(self):
        return self.driver.find_element(submit[0], submit[1])

    def get_skip(self):
        return self.driver.find_element(skip[0], skip[1])


