
    # test_operator_dashboard.py
import pytest
from selenium import webdriver
from flask import g
from flask import session

from flaskr.db import get_db

@pytest.fixture
def driver():
    # Set up your WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    yield driver
    driver.quit()

#BUTTON TESTS

def test_acknowledge_button_exists(driver):
    # Tests if it can find the aknowledge button element in our page 
    driver.get('C:\Manufacturing\Mikael_FLASK_Test\tutorial\flaskr\templates\auth\operator.html')
    acknowledge_button = driver.find_element_by_xpath('//button[text()="Acknowledge"]')
    assert acknowledge_button.is_displayed()

def test_acknowledge_button_click(driver):
    driver.get('C:\Manufacturing\Mikael_FLASK_Test\tutorial\flaskr\templates\auth\operator.html')
    acknowledge_button = driver.find_element_by_xpath('//button[text()="Acknowledge"]')

    # Mock the handleAcknowledgeClick function
    def mock_handle_acknowledge_click():
        # mock implementation (e.g., log a message)
        print("Acknowledge button clicked!")

    # Replace the actual function with the mock
    original_handle_acknowledge_click = test_acknowledge_button_click.handleAcknowledgeClick
    test_acknowledge_button_click.handleAcknowledgeClick = mock_handle_acknowledge_click

    try:
        # Click the button
        acknowledge_button.click()

        # Verify that the mock function was called
        assert "Acknowledge button clicked!" in driver.page_source
    finally:
        # Restore the original function
        test_acknowledge_button_click.handleAcknowledgeClick = original_handle_acknowledge_click

#TABLE TESTS

def test_current_alarms_table_exists(driver):
    #Tests that current alarms table has loaded up and findable 
    driver.get('C:\Manufacturing\Mikael_FLASK_Test\tutorial\flaskr\templates\auth\operator.html')
    current_alarms_table = driver.find_element_by_id('current-alarms')
    assert current_alarms_table.is_displayed()

def test_past_alarms_table_exists(driver):
    #Tests that past alarms table has loaded up and findable 
    driver.get('C:\Manufacturing\Mikael_FLASK_Test\tutorial\flaskr\templates\auth\operator.html')
    past_alarms_table = driver.find_element_by_id('past-alarms')
    assert past_alarms_table.is_displayed()

def test_table_headers(driver):
    #Tests that the table headers have loaded up and are visable  
    driver.get('C:\Manufacturing\Mikael_FLASK_Test\tutorial\flaskr\templates\auth\operator.html')
    headers = driver.find_elements_by_css_selector('table th')
    expected_headers = ['Date', 'Priority', 'Location']
    for header in headers:
        assert header.text in expected_headers