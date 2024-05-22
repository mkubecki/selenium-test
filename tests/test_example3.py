import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_example():
    driver = webdriver.Chrome()
    driver.get("https://www.eduamp.pl")
    assert "eduamp.pl —zkolenia IT i doradztwo w zakresie IT" in driver.title
    driver.quit()