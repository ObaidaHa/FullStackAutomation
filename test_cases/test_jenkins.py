from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"


class Test_browser_connection_01:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://imdb.com")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test01_verify_title(self):
        driver.refresh()
        actual_title = driver.title
        if actual_title == expected_title:
            print("Test 01 - Passed")
        else:
            print("Test 01 - Failed!")
            print("Actual title is:", actual_title)

    def test02_verify_url(self):
        driver.refresh()
        actual_url = driver.current_url
        if actual_url == expected_url:
            print("Test 02 - Passed")
        else:
            print("Test 02 - Failed!")
            print("Actual URL is:", actual_url)