from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Homework #2 (2) path strategies

    #Amazon logo - By.CLASS_NAME, "//a[@class='a-icon a-icon-logo']"

    #Continue Button - By.ID, "//input[@ID='continue']"

    #Need Help Link - By.CLASS_NAME, "//span[@class='a-expander-prompt']"

    #Forgot your password link - By.ID, "//a[@ID='auth-fpp-link-bottom']"

    #Other issues with Sign-In link - By.ID, "//a[@ID='ap-other-signin-issues-link']"

    #Create your Amazon account button - By.ID, "//a[@ID='createAccountSubmit']"

    #Conditions of use link - By.XPATH, "//a[@class='a-link-normal' and @text()='Conditions of Use']"

    #Privacy Notice link - By.XPATH, "//a[@class='a-link-normal' and @text()='Privacy Notice']"
#End Task 2


#Test Case for Help search using python & selenium script

driver = webdriver.Chrome(executable_path="C:\\Users\\fitle\\Desktop\\Automation Course\\python-selenium-automation\\chromedriver")

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')
driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)


actual_result = driver.find_element(By.XPATH, "//a[@name='GUID-159D403A-3B08-477C-88E3-58C737822D49']").text
expected_result = driver.find_element(By.XPATH, "//a[@name='GUID-159D403A-3B08-477C-88E3-58C737822D49']").text
#False Condition to use
#expected_result = 'Cancel Orders'

assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'

print('Test case passed')
driver.quit()
