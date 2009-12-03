"""
Copyright 2006 ThoughtWorks, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Diff functions needed
---------------------
Login as teacher / location etc etc


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
        sel.open("https://stage15.pendalearning.com")
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
