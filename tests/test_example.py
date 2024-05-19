import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_example():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title
    driver.quit()