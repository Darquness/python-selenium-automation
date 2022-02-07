# Task 1A -  Logged out user sees Sign in page when clicking Orders rewritten for Page Objects

# BDD File
'''
Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened
'''

# Step page usage
'''
@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open()


@when("Click amazon orders Link")
def click_orders(context):
    context.app.header.click()


@then("Verify Sign In page is opened")
def verify_search_result(context, expected_result):
    context.app.results_page.verify_search_result(expected_result)
'''

# main_page usage
'''
from Pages.base_page import Page

class MainPage(Page):

    def open(self):
        self.open_page("https://www.amazon.com/")
'''

# Header page usage
'''
from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Header(Page):

	ORDERS_ICON = (By.ID, "nav-orders")
	
	
    def click_orders(self):
		self.click(*self.ORDERS_ICON)
'''

# results_page usage
'''
from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)
'''

# Applications page usage
'''
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.results_page import SearchResults

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header()
        self.main_page = MainPage()
        self.results = SearchResults(self.driver)
'''

# base_page usage
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, end_url=''):
        print(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Got this text: {actual_text}, did not match {expected_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'
'''

	

