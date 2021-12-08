#imports
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
'''

#driver usage
#driver = webdriver.Chrome(executable_path="C:\\Users\\fitle\\Desktop\\Automation Course\\python-selenium-automation\\chromedriver")


#Task 1 Begin - Create a test case that will open amazon BestSellers page
#Task 1 Feature file data
'''
Feature: Test Best Sellers links at top of page appearance

  Scenario: User can see the links near the top of Best Sellers page
    Given Open Amazon page
    When Click on Best Sellers link
    Then Verify 5 links on Best Sellers page
'''

#Task 1 Python data file
'''
BS_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab'] a[href]")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers link')
def click_best_sellers_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']").click()


@then('Verify {expected_amount} links on Best Sellers page')
def verify_best_sellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    link_count = context.driver.find_elements(*BS_LINKS)
    assert len(link_count) == expected_amount, f'Expected to see {expected_amount} elements, but got {len(link_count)}'
'''
#End Task 1


#Task 2 Begin - Create your own test case to add any product you want into the cart, and make sure it’s there
#Task 2 Feature file data
'''
Feature: Test to see if user can add a product to the cart
  # Enter feature description here

    Scenario: User can add a product to the shopping cart
    Given Open Amazon page
    When Search for plates
    And Click on the first product
    And Click on One Time Purchase
    And Click on Add to Cart button
    And Open cart page
    Then Verify cart has 1 item(s)
'''

#Task 2 Python file data
'''
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-impression-counter']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')


@when('Search for plates')
def search_plates(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('plates', Keys.RETURN)


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on One Time Purchase')
def click_One_time_purchase(context):
    context.driver.find_element(By.CSS_SELECTOR, "i[class*='a-icon a-accordion").click()


@when('Click on Add to Cart button')
def click_add_to_cart_(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error, actual {actual_count} did not match {expected_count}'
'''
#End Task 2