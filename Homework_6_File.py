# Task 1 - Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions

# BDD Feature File
'''
  Scenario: User can open and close Amazon Privacy Notice
    Given Open T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
'''

# Python File
'''
# import support
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open T&C page')
def open_amazon_TandC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window:', context.orignal_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


# I chose the header verification as the page name itself was very similar to the original page name.
# So I want to use a bettre verification target instead
@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[class='help-content'] h1")
    expected_header = 'Amazon.com Privacy Notice'
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "div[class='help-content'] h1")
    assert expected_header == actual_header, f'Error! Expected {expected_header} but got {actual_header}'


@then('User can close new window and switch back to original')
def back_to_original_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
'''
