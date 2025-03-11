from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import  Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_button_display(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()