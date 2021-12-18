'''
from selenium.webdriver.common.by import By
from behave import given, when, then
'''

#Task 1 - Remove sleeps from previous coding and replace with implicit or explicit wait coding
'''
    My previous assignments I turned in did not have any sleep usage in them. 
    I did remove sleeps from the class/lectures and replaced with wait coding
'''
#End Task 1

#Task 2 - Make a test case with a loop. You can use color selection for any product page you like.

#Task 2 Feature File
'''
Feature: Test for product page

  Scenario: User can select product colors
    Given Open Amazon B088K8LFHD page
    Then Verify user can click through colors
'''

#Task 2 Python File
'''
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given ('Open Amazon {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Charcoal Heather', 'Heather Blue', 'Heather Light Olive', 'Heather Pink']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    
    actual_colors = []
        for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]
        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors}, but got {actual_colors}'
    # For false assertion testing, I would change one of the colors to produce error message like 'Heather Dark Olive'
    # as the second color.
'''
#End Task 2


#Task 4 - Create a function that will take a string as an input and return the 1st non-unique letter of a string.

#Python program

# Setting the maximum size of the array
arraySize = 256


# Creating the array, passing the string into it, counting the total characters use for the string
'''
def totalString(string):
    totalChars = [0] * arraySize
    for i in string:
        totalChars[ord(i)] += 1

    return totalChars


# Provides the first non-repeating index (index number) in the string array or provides no repeating characters (-1)
def stringTraversal(string):
    totalChars = totalString(string)
    index = -1
    k = 0

    for i in string:
        if totalChars[ord(i)] == 1:
            index = k
            break
        k += 1
        # print(k)

    return index


# Code that uses previous functions for string traversal to confirm
# the first unique character or none at all from user input
string = str(input("Enter string: "))

# "total" is number of characters from string + 1.
# This is to match the -1 value of index from the stringTraversal function if there are no unique characters
total = len(string) - (len(string) + 1)
index = stringTraversal(string)
if index == total:
    print(" ")

else:
    print("First non-repeating character is " + string[index])
'''

#Task 4 Questions
# How would you test it?
'''
I would input a string that has no unique characters to make sure the non-unique character outcome is triggered. 
This is done by using the false value, or -1 returned as index, from the stringTraversal function. Then, getting the 
length from the inputted string and subtracting 1 more then the total length so it matches the -1 value from 
stringTraversal.

Then I would add a unique character in the middle of the string to trigger the the unique character outcome. Because,
is taking the user input as a string, I would add a test case for a number and a special character.

'''

# How would you handle edge cases?
'''
After getting the unique character outcome from adding a unique character in the middle of the string, I would add an
additional unique character at the beginning of the string to confirm at character is the one the program finds first.
Then, I would erase the unique character from the beginning and add a different unique character at the end.
I should get the unique character in the middle as the outcome again. I would erase the middle unique character and run the
program again to get the unique character at the end as the expected outcome.

Example tests:
    First input- reddress       outcome - " "
    
    Second input - readdress    outcome - First non-repeating character is a
                     ^
    Third input- ureaddress     outcome - First non-repeating character is u
                 ^
    Fourth input- readdresst    outcome - First non-repeating character is a
                    ^       \-new input
                    
    Fifth input- reddresst      outcome - First non-repeating character is t
                         ^
    Sixth input- reddre3ss      outcome - First non-repeating character is 3
                       ^                         
    Seventh input- reddress/    outcome - First non-repeating character is /
                           ^
    Eigth input- $$nneess       " "
'''
#End Task 4