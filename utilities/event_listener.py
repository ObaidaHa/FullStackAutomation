from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("Before Navigate to", url)

    def after_navigate_to(self, url, driver):
        print("After Navigate to", url)

    def before_navigate_back(self, driver):
        print("Before Navigate Back", driver.current_url)

    def after_navigate_back(self, driver):
        print("After Navigate Back", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before Navigate Forward", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After Navigate Back", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before Find Element", value)

    def after_find(self, by, value, driver):
        print("After Find Element", value)

    def before_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print("Before Change Value", element.get_attribute("value"))
        else:
            print("Before Change Value", element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print("After Change Value", element.get_attribute("value"))
        else:
            print("After Change Value", element.text)

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute("value")
        if element.tag_name == 'input':
            print("Before Click", EventListener.button_text)
        else:
            print("Before Click", EventListener.button_text)

    def after_click(self, element, driver):
        print("After Click", EventListener.button_text)

    def before_execute_script(self, script, driver):
        print("Before Execute Script", script)

    def after_execute_script(self, script, driver):
        print("After Execute Script", script)

    def before_close(self, driver):
        print("Before Closing Tab")

    def after_close(self, driver):
        print("After Closing Tab")

    def before_quit(self, driver):
        print("Before Quiting session")

    def after_quit(self, driver):
        print("After quitting session")

    def on_exception(self, exception, driver):
        print("On Exception" + str(exception))
