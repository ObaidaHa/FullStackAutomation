from selenium.webdriver.common.by import By

name = (By.CSS_SELECTOR, "input[id='name-input']")
email = (By.CSS_SELECTOR, "input[id='email-input']")
user_name = (By.ID, "username-input")
password = (By.CSS_SELECTOR, "input[id='password-input']")
create_user = (By.CSS_SELECTOR, ".css-sqvqs4-button")


class ServerAdminNewUser:
    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(name[0], name[1])

    def get_email(self):
        return self.driver.find_element(email[0], email[1])

    def get_user_name(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password_new(self):
        return self.driver.find_element(password[0], password[1])

    def get_create_user(self):
        return self.driver.find_element(create_user[0], create_user[1])
