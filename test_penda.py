"""

Diff functions needed
---------------------
Login as teacher / location etc etc

Penda test
----------
Go through as 4 users to 


schools = ['fldemo', 'cademo']
users   = [('admin','sam'), ('teacher','teacher')]

"""

from selenium import selenium
import unittest
import HTMLTestRunner



class TestSam(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "https://www.samlearning.com")
        self.selenium.start()
        
    def test_sam_login(self):
        sel = self.selenium
        #override default 30s timeout (!)
        sel.set_timeout(60000)  # not same in python client as documents...
        sel.open("https://sam:sam@stage15.pendalearning.com")

        sel.type("centerId", "cademo")
        sel.type("login", "admin")
        sel.type("password", "sam")

        sel.click("submit")
#long load time...
        sel.wait_for_page_to_load(60000)
#        self.assertEqual("", sel.get_title())
#        self.assertTrue(sel.is_text_present("Welcome"))
        print sel.get_title()
        print "+++"

#        print sel.get_text("xpath=id('footerStatisticsLayout')")
        print sel.get_text("xpath=id('contentFrame')/div[6]/div[1]/b") 
        print sel.get_text("xpath=id('contentFrame')/div[7]/div[1]/b") 
        print sel.get_text("xpath=id('contentFrame')/div[8]/div[1]/b") 
        print sel.get_text("xpath=id('contentFrame')/div[9]/div[1]/b") 

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
#    HTMLTestRunner.main()
