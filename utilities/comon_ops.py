import csv
import os
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


################################################
# Function Name: get_data
# Function Description: Retrieves a value from an XML file based on the node name
# Function Parameters: node_name (str): The name of the node whose value needs to be fetched from the XML
# Function Return: str: The text value of the specified XML nod
################################################
def get_data(node_name):
    root = ET.parse('C:/Users/Obaida/Documents/MyProject/FullStackAutomation/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


################################################
# Function Name: wait
# Function Description: Waits for a specific condition on an element to be met
# Function Parameters:
#   - for_element (str): The condition to wait for elements
#   - elem (tuple): The locator of the element
################################################
def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(Ec.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            Ec.visibility_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_clickable':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            Ec.element_to_be_clickable((elem[0], elem[1])))


################################################
# Function Name: read_csv
# Function Description: Reads data from a CSV file and returns it as a list of rows
# Function Parameters: file_name (str): The path of the CSV file to be read
# Function Return: list: A list of rows, where each row is a list of cell values
################################################
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


################################################
# Function Name: get_time_stamp
# Function Description: Returns the current time as a timestamp
# Function Return: float: The current time in seconds since the epoch
################################################
def get_time_stamp():
    return time.time()


# Enum for selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_CLICKABLE = 'element_clickable'


# Enum for selecting row from table to delete
class By:
    USER = 'user'
    INDEX = 'index'


# Enum for selecting whether we want to save mortgage transaction or not
class Save:
    YES = True
    NO = False


# Enum for selecting direction of movement (e.g., for swiping or scrolling)
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
