from selenium.webdriver.common.by import By

search = (By.CSS_SELECTOR, ".css-fcoerl-input-input")
clear = (By.CSS_SELECTOR, "button[class='css-1v4tdv6-button']")
new_user = (By.CSS_SELECTOR, "a[href='admin/users/create']")
users_list = (By.XPATH, "//table[@class='filter-table form-inline filter-table--hover']/tbody/tr")
user_by_user_name = (By.CSS_SELECTOR, "a[title='kuku']")
delete = (By.XPATH, "//div/button[@class='css-19vct9a-button']")
confirm_delete = (By.CSS_SELECTOR, "button[aria-label='Confirm Modal Danger Button']")


class ServerAdminPage:
    def __init__(self, driver):
        self.driver = driver

    def get_search(self):
        return self.driver.find_element(search[0], search[1])

    def get_clear_search(self):
        return self.driver.find_element(clear[0], clear[1])

    def get_new_user(self):
        return self.driver.find_element(new_user[0], new_user[1])

    def get_users_list(self):
        return self.driver.find_elements(users_list[0], users_list[1])

    def get_user_by_index(self, index):
        return self.get_users_list()[index]

    def get_user_by_user_name(self, user):
        return self.driver.find_element(user_by_user_name[0], user_by_user_name[1].replace('kuku', str(user)))

    def get_delete_user(self):
        return self.driver.find_element(delete[0], delete[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])

