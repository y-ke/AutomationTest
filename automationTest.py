from selenium import webdriver
import unittest
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

def searchRank(searchInput, targetSite):
    searchKeywords = searchInput.replace(' ', '+')

    browser = webdriver.Chrome("/Users/yujingke/Documents/GitHub/AutomationTest/chromedriver")

    pages = 2

    for i in range(pages):

        browser.get("https://www.google.com/search?q=" + searchKeywords + "&start=" + str(i * 10))
        urlList = []

        for el in browser.find_elements_by_class_name("r"): # find search result entries by class name

            a = el.find_elements_by_tag_name('a')

            urlList.append(a[0].get_attribute("href"))

            print(a[0].tag_name, '--', a[0].text, a[0].get_attribute("href"), '\n') # all the google result searched so far
            # may be blank because google might have certain special results (google jobs etc)

            if a[0].get_attribute("href") == targetSite: 
                # print(urlList)
                print('The rank on the page is ', len(urlList))
                print('The page number is ', i + 1)
                return [i + 1, len(urlList)]
    return 0


class TestSearchRankMethods(unittest.TestCase):

    def testSearchRank(self):
        searchInput = "instawork"
        targetSite = 'https://www.instawork.com/'
        self.assertEqual(searchRank(searchInput, targetSite), [1, 1])

   

if __name__ == '__main__':
    unittest.main()