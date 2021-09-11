import unittest
import re
import subprocess

import basic_stats as bs

basic_stats = "basic_stats.py"
wc = "wc.py"
most_times="most_times.py"

class TestBasicStats(unittest.TestCase):
    def test_basic_avg(self):
        self.assertAlmostEqual(bs.avg([23,32,43,54]),38.0,2,"Your avg function is not working correctly")
    
    def test_one_liners(self):
        code = open(basic_stats).read()
        found = re.findall(r'def (avg|var|l_sqr).+\n\s+(return.+)',code)
        print("ONE LINERS:",found)
        self.assertEqual(len(found),3)

    def test_no_imports(self):
        code = open(basic_stats).read();
        found = re.findall(r'(import .+)',code)
        print ("IMPORTS:",found)
        self.assertTrue(len(found)<1,"Your code should have no imports")

    def test_l_sq(self):
        self.assertEqual(sum(bs.l_sqr([23,32,43,54])),6318,"Your Least Squares is not correct")

    def test_var(self):
        self.assertAlmostEqual(bs.var([23,32,43,54]),135.5,2,"Your VAR function is not correct")

    def test_dicts(self):
        code = open(wc).read()
        found = re.findall(r'(.+=.+(dict\(\)|\{))',code)
        print("DICTIONARIES:",found)
        self.assertTrue(len(found)>0)

    def test_wc(self):
        text= """The good news is, you’ve probably already created a test without realizing it. Remember when you ran your application and used it for the first time? Did you check the features and experiment using them? That’s known as exploratory testing and is a form of manual testing.

        Exploratory testing is a form of testing that is done without a plan. In an exploratory test, you’re just exploring the application.

        To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it.

        That doesn’t sound like much fun, does it?

        This is where automated testing comes in. Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human. Python already comes with a set of tools and libraries to help you create automated tests for your application. We’ll explore those tools and libraries in this tutorial."""
        open("test_file.txt","w").write(text)
        word_counts = subprocess.run(["python","wc.py","test_file.txt"],stdout=subprocess.PIPE, text=True)
        print("WC OUTPUT:",word_counts)
        f = input("Printed lines:9, unique:125, words:238, chars:1202\n Most frequent word:(28 times), Less frequent word:The(1 times)? (Y/N)")
        self.assertEquals(f,'Y',"Word counts did not match")

    def test_most_frequent(self):
        out = subprocess.run(["python","most_times.py","4", "6", "7", "5", "4", "3", "5", "1", "4", "5", "7", "4", "2"], stdout=subprocess.PIPE,text=True)
        print("MOST TIMES:",out)
        self.assertEqual(out.returncode,0)
        self.assertTrue(out.stdout.find("4")>-1,"Your most frequent algorihtm fails")

if __name__=="__main__":
    unittest.main()