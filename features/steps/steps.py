from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

@given('Open page')
def open_page(context):
    chrome_driver_path = "/Users/dimatsy/Downloads/chromedriver-mac-arm64/chromedriver"
    service = webdriver.chrome.service.Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)

@when('Open page')
def open_page_1(context):
    context.driver.get("https://www.saucedemo.com/")

@when('Enter username and password')
def till(context):
    Login = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'user-name'))
    )
    Login.send_keys('standard_user')

    Psw = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    Psw.send_keys('secret_sauce')


@then('Click login button and assert')
def button_and_check(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-button'))
    )
    button.click()
    try:
        test_text = context.driver.find_element(By.CLASS_NAME, 'app_logo').text
        assert test_text == 'Swag Labs', "False - "
        print("True + ")
    except Exception as e:
        print("Bag", e)

@then('Quit browser')
def step_impl(context):
    context.driver.quit()
