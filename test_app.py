from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_homepage():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000")

    assert "CI/CD Pipeline Working" in driver.page_source

    print("Homepage test passed")

    driver.quit()

def test_title():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000")

    assert driver.title is not None

    print("Title test passed")

    driver.quit()

test_homepage()
test_title()
