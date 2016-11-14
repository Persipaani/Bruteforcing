'''
Created on 2016

@author: Sampo

A simple program that bruteforces itnry.co combinations to find working ones
Maybe itnry.co should increase amount of random letters & numbers?

Note:
!!! I TAKE NO RESPONSIBILITY ON ANY PAGES THAT THIS PROGRAM MIGHT LEAD YOU
USE AT YOUR OWN RISK! DESPITE THE NAME THIS PROGRAM DOES NO HACKING BUT JUST
SHOWS HOW WEAK A SHORT STRING IS TO BRUTEFORCE !!!

'''

import urllib.request
import http.client
import time
import os
import string
import random

class checker(object):
    
    def __init__(self):
        self.url=""
        self.endings=[]
        self.working_urls = []
        self.run()
        
    
    def run(self):
        self.working_urls = []
        input_value = input("Enter how many you want \n")
        amount = int(input_value)
        current = 0.0
        prev_prog = 0.0
        working = False
        
        start_time = time.time()
        
        a = 1
        while(len(self.working_urls)<amount):
            cur_prog = round((current/amount)*100,0)
            if(cur_prog != prev_prog):
                print(str(cur_prog) + " %")
            prev_prog = cur_prog
            a+=1
            
            generated_string = self.generateTinyurl()
            print("Trying: " + generated_string)
            working = self.check_this("http://itnry.co/" + generated_string)
            if(working):
                current+=1
            print("-------------------")
            
        end_time = time.time()
        
        print("This took: " + str(end_time-start_time) + " seconds. \n")
        
        if(len(self.working_urls)!=0):
            print("Working: ")
            for a in range(len(self.working_urls)):
                print(str(self.working_urls[a]))
            input("Press Enter to quit")
    
    def generateTinyurl(self):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(4))
        
    def check_this(self,url):
        html_file = None
        try:
            html_file, headers = urllib.request.urlretrieve(url)
        except urllib.error.HTTPError as error:
            if(str(error) == "HTTP Error 404: Not Found"):
                print("404")
                return False
            if(str(error) == "HTTP Error 403: Forbidden"):
                print("403")
                self.working_urls.append(url)
                return True
            else:
                print(error)
        except:
            print("Other Error")
            return False #Not sure but i think so
        
        if(html_file != None):
            print("Got something...")
            if(self.read_html_file(html_file)):
                self.working_urls.append(url)
                return True
            else:
                return False
        else:
            return False
        
    def read_html_file(self,file):
        html = open(file)
        line_contains = ""
        linecount=0 #keeps count of read lines
        
        try:
            for line in html:
                linecount+=1
                if(linecount==123):
                    print("Preview: " + line)
                    line_contains = line
            if(line_contains=="<h1>Error: Unable to find site's URL to redirect to.</h1>"):
                return False
            else: 
                return True
        except:
            print("Failure in reading HTML")
            return True

checker()