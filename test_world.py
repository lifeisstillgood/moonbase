"""

Diff functions needed
---------------------
Login as teacher / location etc etc

Penda test
----------
Go through as 4 users to 



090191BA
https://stage13.samlearning.com:8444/content/test/show/contentId/100607
id('sidebarMarkMyWork')
id('sidebarMarkMyWork')
"""

from selenium import selenium
import unittest
import HTMLTestRunner

schools = ['fldemo', 'cademo', 'dcdemo', 'gademo', 'mademo','midemo','msdemo','modemo',
           'nydemo', 'txdemo', 'vademo']
users   = [('admin','sam'), ('teacher','teacher'),
           ('010101aa', '010101aa'),]
log = 'foo.log'

examURL = 'https://stage13.samlearning.com:8444/content/test/show/contentId/100607'

class TestSam(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "https://www.samlearning.com")
        self.selenium.start()

    def test_exam(self):
        '''given school username and password, see what the boxchildren are '''
        sel = self.selenium
        #override default 30s timeout (!)
        sel.set_timeout(60000)  # not same in python client as documents...
        sel.open("https://stage13.samlearning.com")

        sel.type("centerId", 'samsec')
        sel.type("login", '090191BA')
        sel.type("password", '090191BA')
        sel.click("submit")

        sel.wait_for_page_to_load(60000)

#            box1title = sel.get_text("xpath=id('contentFrame')/div[6]/div[1]/b") 
#            sel.click("xpath=id('contentMenu1')/div/div[5]/a")
   
        sel.open(examURL)
        sel.wait_for_page_to_load(60000)
        sel.click("xpath=id('sidebarMarkMyWork')")
        

    def tearDown(self):
        #self.selenium.stop()
        pass
if __name__ == "__main__":
    unittest.main()
#    HTMLTestRunner.main()
