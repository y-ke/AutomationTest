# AutomationTest

## Project

Using your language / test framework of your choice, create test(s) to validate Instawork (www.instawork.com) appears first in a Google search for a given keyword.

If we do not appear first, the test should find out which position on the list our site appears in the search results.

### Bonus Points
Support multiple browsers

Accept google search terms as input

Support finding position of the site across search pages


## Solution

I used Python Selenium framework and unit testing tools in this project. The function will search the first two pages of the Google search result (it could also be easily modified if we change "pages" variable).

If the exact result matching target site is found, the corresponding rank on the page and the page will be printed and returned. Otherwise we return 0.

The automationTest.py does not allow user input to customize via Terminal but the automationTestWithInput.py does. 

### How to run
First you might need python 3 ready to use. Here I had Anaconda python 3 environment. Second in this project I tested with Chrome. Lastly Selenium framework should be installed according to your system environment. For me I used pip install command "pip install -U selenium" and downloaded the webdriver. More details could be found here: https://chromedriver.chromium.org/getting-started.

After downloading this repo, change directory into the folder, and in terminal type "python3 automationTest.py" or "python3 automationTestWithInput.py" to run each file. The output will be shown in the terminal.

### Example Output

a -- www.instawork.com

Instawork - Find work at local businesses in less than 24 hours ... https://www.instawork.com/ 

The rank on the page is  1

The page number is  1


----------------------------------------------------------------------

Ran 1 test in 4.113s

OK
