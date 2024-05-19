import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://eduamp.pl")
    assert "Selenium WebDriver" in driver.title
    driver.quit()