'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
'''

#Task 1 - find best CSS Selector for each section
'''
Amazon logo by "i.a-icon[aria-label='Amazon']"

Create Account logo by "h1.a-spacing-small"

Your Name textbox by "input#ap_customer_name"

Email textbox by "input#ap_email"

Password textbox by "input#ap_password"

Password requirements by "div.auth-inlined-information-message div.a-alert-content"

Re-enter password textbox by "input#ap_password_check"

Create account button by "input#continue"

Conditions link by "a[href*='ap_register_notification_condition_of_use']"

Privacy link by "a[href*='ap_register_notification_privacy_notice']"

Sign in link by "a[href*='openid.return_to']"
'''
#End Task 1

#Task 2 - Update test case for support search using BDD

#Task 2 feature file data
'''
Feature: Test help search results

  Scenario: User can get to Cancel orders page
    Given Open Amazon Support page
    When Search Cancel Order
    Then Verify Cancel Order page appears
'''
#Task 2 Python file
'''
@given('Open Amazon Support Page')
def open_amazon_support(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search Cancel Order')
def search_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.RETURN)


@then('Verify Cancel Order page appears')
def verify_Cancel_Orders_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[class='help-content']")
    expected_header = 'Cancel Items or Orders'
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h1")
    assert actual_header == expected_header, f'Error, actual {actual_header} did not match {expected_header}'


'''
#Task 2 end

#Task 3 - Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.

#Task 3 Feature file data
'''
Feature: Test to see if cart is empty on Amazon

  Scenario: User can verify if cart is empty on Amazon
    Given Open Amazon page
    When Click Shopping Cart
    Then Verify Shopping Cart is empty
'''

#Task 3 Python file data
'''
@given('Open Amazon page')
def open_amazon_support(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Shopping Cart')
def click_shopping_cart(context):
    context.driver.find_element(BY.CSS_SELECTOR, "a[href*='nav_cart']").click()


@then('Verify Shopping Cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(BY.CSS_SELECTOR, "a[id='a-autoid-0-announce']")
    expected_header = 'Your Amazon Cart is empty'
    actual_header = context.driver.find_element(BY.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")
    assert expected_header == actual_header, f'Error! Expected {expected_header} but got {actual_header}'


'''
#Task 3 end
