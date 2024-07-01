import time

import pytest
from selenium import webdriver


# @pytest.fixture
# def setup_teardown():
#     print("Launch Browser")
#     print("Open App")
#     yield
#     print("Close App")
#     print("Close Browser")


# def test_set1(setup_teardown):
#     print("Main App...")

def setup_function(function):
    print("Setup Function...")

def teardown_function(function):
    print("Teardown Function...")

def setup_module(module):
    print("Setup Module..")

def teardown_module(module):
    print("Teardown Module..")

def test_set2():
    print("Main app set2")

def test_set3():
    print("Main app set3")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()

def test_set4():
    print("Main app set3")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    time.sleep(5)
    driver.quit()

def test_set5():
    print("Main app set3")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yahoo.in")
    time.sleep(5)
    driver.quit()