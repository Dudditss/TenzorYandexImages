import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:/Users/Alex/Desktop/chromedriver.exe")
    yield driver
    driver.quit()
