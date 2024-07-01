import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_assertion():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    time.sleep(4)
    expected_title = "Facebook – log in or sign up"
    actual_title = driver.title
    assert expected_title.__eq__(actual_title)
    time.sleep(3)
    # driver.find_element(By.XPATH("//img[contains(@class, 'fb_logo')]"))
    # str1 = driver.find_element(By.XPATH('//a[@role="button" and contains(@class,"_51sy") and @id="u_0_0_LE"]')).text
    str1 = driver.find_element(By.XPATH, '//a[@role="button" and contains(@class,"_51sy") and @id="u_0_0_LE"]').text

    print(str1)
    driver.quit()