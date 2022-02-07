# Task 1 - Make another test scenario using a dropdown and search for an item in a different Amazon department.

# Dropdown BDD File
'''
  Scenario: User can search for an item in a different Amazon department using the search dropdown.
    Given Open Amazon Page
    When Choose Amazon Devices from department dropdown
    And Search for Kindle
    And Click search icon
    Then Verify Amazon Devices department is selected
'''
	
# Dropdown PO steps file
'''
from behave import given, when, then

@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open()


@when("Choose {dept} from department dropdown")
def select_dept(context, dept):
    context.app.header.select_dept(dept)


@when("Search for {keyword}")
def search_amazon(context, keyword):
    context.app.header.search_input(keyword)


@when("Click search icon")
def click_search(context):
    context.app.header.click_search()


@then("Verify {category} department is selected")
def verify_dept(context, category):
    context.app.results_page.verify_correct_dept(category)
'''

# Main page
'''
from Pages.base_page import Page

class MainPage(Page):

    def open(self):
        self.open_page("https://www.amazon.com/")
'''

# base_page
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

    def open_page(self, end_url):
        print(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))
'''

# Application
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

# header
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.base_page import Page

class Header(Page):
	
	SEARCH_INPUT = (By.ID, "twotabsearchbox")
	SEARCH_ICON = (By.ID, "nav-search-submit-button")
	DEPT_OPTION = (By.ID, "searchDropdownBox")
	
	def search_amazon(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)
	
	def select_dept(self, dept: str):
        dropdown = self.find_element(*self.DEPT_OPTION)
        select = Select(dropdown)
        select.select_by_value(f'search-alias={dept}')
'''

# results_page
'''
from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SearchResults(Page):
	
	CORRECT_DEPT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
	 
	def _get_cat_locator(self, category):
        return [self.CORRECT_DEPT[0], self.CORRECT_DEPT[1].replace('{CATEGORY}', category)]
		
	def verify_correct_dept(self, category):
        locator = self._get_cat_locator(category)
        self.wait_for_element_appear(*locator)
'''
# Task 1 End


# Task 2 - Make a test case that: Opens https://www.amazon.com/gp/product/B074TBCSC8 , hovers over New Arrivals, 
#          then verifies that the user sees the deals.

# Deals BDD File
'''
  Scenario: User can see the deals while hovering over New Arrivals
    Given Open Amazon Page
    When Hover over New Arrivals
    Then Verify New Arrivals deals appear
'''

# Deals step file
'''
@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open()

@when("When Hover over New Arrivals")
def hover_arrivals(context):
    context.app.header.hover_arrivals()

@then("Verify New Arrivals deals appear")
def verify_arrival_deals_present(context):
    context.app.header.verify_arrival_deals_present()
'''

# Main page
'''
from Pages.base_page import Page

class MainPage(Page):

    def open(self):
        self.open_page("https://www.amazon.com/gp/product/B074TBCSC8")
'''

# base_page
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

    def open_page(self, end_url):
        print(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))
'''

# Application
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

# header
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.base_page import Page

class Header(Page):

# I used this command after learning how to get to specific child selectors 
# $$("#nav-subnav > a:nth-child(7) > span.nav-a-content")
ARRIVALS = (By.CSS_SELECTOR, "#nav-subnav > a:nth-child(7) > span.nav-a-content")
	
	def hover_arrivals(self):
        arrivals = self.find_element(*self.ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(arrivals)
        actions.perform()

    def verify_arrival_deals_present(self):
        self.wait_for_element_appear(*self.ARRIVALS)
'''
# Task 2 - End

