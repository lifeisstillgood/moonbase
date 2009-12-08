"""

Diff functions needed
---------------------
Login as teacher / location etc etc

Penda test
----------
Go through as 4 users to 




"""

from selenium import selenium
import unittest
import HTMLTestRunner

schools = ['fldemo', 'cademo', 'dcdemo', 'gademo', 'mademo','midemo','msdemo','modemo',
           'nydemo', 'txdemo', 'vademo']
users   = [('admin','sam'), ('teacher','teacher'),
           ('010101aa', '010101aa'),]
log = 'foo.log'

class TestSam(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "https://www.samlearning.com")
        self.selenium.start()

    def postlogin(self, school, user, passwd):
        '''given school username and password, see what the boxchildren are '''
        sel = self.selenium
        #override default 30s timeout (!)
        sel.set_timeout(60000)  # not same in python client as documents...
        sel.open("https://sam:sam@stage15.pendalearning.com")

        sel.type("centerId", school)
        sel.type("login", user)
        sel.type("password", passwd)
        sel.click("submit")

        sel.wait_for_page_to_load(60000)

        if user != '010101aa':
            box1title = sel.get_text("xpath=id('contentFrame')/div[6]/div[1]/b") 
            box2title = sel.get_text("xpath=id('contentFrame')/div[7]/div[1]/b") 
            box3title = sel.get_text("xpath=id('contentFrame')/div[8]/div[1]/b") 
            box4title = sel.get_text("xpath=id('contentFrame')/div[9]/div[1]/b")
        else:
            box1title = sel.get_text("xpath=id('funContainer')/div/div[2]/div[1]/b") 
            box2title = sel.get_text("xpath=id('funContainer')/div/div[3]/div[1]/b") 
            box3title = sel.get_text("xpath=id('funContainer')/div/div[4]/div[1]/b") 
            box4title = sel.get_text("xpath=id('funContainer')/div/div[5]/div[1]/b")
       
        fo = open(log, 'ab')
        s = "%s-%s:\t%s\t%s\t%s\t%s" % (school, user, box1title, box2title,
                                        box3title, box4title)
        fo.write(s + "\n")
        fo.close()
        if user != '010101aa':
            sel.click("helpMenuLogout") 
        else:
            sel.click("xpath=id('contentMenu1')/div/div[5]/a")
   
    def test_titles(self):
        ''' '''
        for school in schools:
            for user, passwd in users:
                print user, passwd, school
                self.postlogin(school, user, passwd)

    x='''
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
    '''
    
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
#    HTMLTestRunner.main()
