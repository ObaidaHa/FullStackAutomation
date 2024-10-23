import os
import time

import allure
import mysql.connector
import selenium
import pytest
import selenium.webdriver
import appium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
# from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.comon_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None
action2 = None
m_action = None
mobile_size = None
db_connector = None


# eyes = Eyes()  # Applitools


# Fixture to initialize web driver for web testing
@pytest.fixture(scope='class')
def init_web_driver(request):
    if get_data('ExecuteApplitools').lower() == 'yes':
        globals()['driver'] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()

    # if get_data('ExecuteApplitools').lower() == 'yes':
    #     eyes.api_key = get_data('ApplitoolsKey')
    yield
    driver.quit()
    # if get_data('ExecuteApplitools').lower() == 'yes':
    #     eyes.close()  # applitools
    #     eyes.abort()  # applitools


# Fixture to initialize mobile driver for mobile testing
@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()

    yield
    driver.quit()


# Fixture to initialize electron driver for electron app testing
@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


# Fixture to initialize desktop driver for desktop app testing
@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


# Fixture to initialize database connection for testing
@pytest.fixture(scope='class')
def init_db_connection(request):
    db_connector = mysql.connector.connect(
        host=get_data('DB_Host'),
        database=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Password')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


# Function to get the web driver based on browser type
def get_web_driver():
    web_driver = get_data('Browser')
    # web_driver = os.getenv('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong Input, Unrecognized Browser!')
    return driver


# Function to get the mobile driver based on device type
def get_mobile_driver():
    if get_data('MobileDevice').lower() == 'android':
        driver = get_android(get_data('udid'))
    elif get_data('MobileDevice').lower() == 'iOS':
        driver = get_ios(get_data('udid'))
    else:
        driver = None
        raise Exception('Wrong Input, Unrecognized Mobile OS!')
    return driver


# Function to get the electron driver
def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('ElectronApp')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('ElectronDriver'))
    return driver


# Function to get the desktop driver for Windows applications
def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('ApplicationName')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    dc['automationName'] = 'Windows'
    driver = appium.webdriver.Remote(get_data('WinAppDriverService'), dc)
    return driver


# Function to get the Chrome web driver
def get_chrome():
    # srv = Service(ChromeDriverManager().install())         # selenium 4.X
    # chrome_driver = selenium.webdriver.Chrome(service=srv) # selenium 4.X
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())  # selenium 3.X
    return chrome_driver


# Function to get the Firefox web driver
def get_firefox():
    # srv = Service(executable_path=GeckoDriverManager().install()) # selenium 4.X
    # firefox_driver = selenium.webdriver.Firefox(service=srv)      # selenium 4.X
    firefox_driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())  # selenium 3.X
    return firefox_driver


# Function to get the Edge web driver
def get_edge():
    # srv = Service(EdgeChromiumDriverManager(log_level=20).install())    # selenium 4.X
    # edge_driver = selenium.webdriver.Edge(service=srv)      # selenium 4.X
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())  # selenium 3.X
    return edge_driver


# Function to get the Android driver for mobile testing
def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('AppPackage')
    dc['appActivity'] = get_data('AppActivity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('AppiumServer'), dc)
    return android_driver


# Function to get the iOS driver for mobile testing
def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('BundleID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('AppiumServer'), dc)
    return ios_driver


# Hook to capture screenshots on test failure and attach them to Allure report
# catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None -> this is exception from API test
            image = get_data("ScreenshotPath") + 'screen_' + str(get_time_stamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
