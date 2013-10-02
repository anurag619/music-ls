#!/usr/bin/env python

import fbconsole
import re
import time
import sys
from google import search
from random import choice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    print "do you wish to add some songs yourself or listen according to your likes?"
    choice = raw_input("A--> to add songs \nL--> listen according to your likes. \nEnter your choice:  ")
    if choice == 'A':
     user_input_name = input("Enter your song/artist: ").split(',')     
     for name in user_input_name:
      print "please wait while we search for your entries"
      song_name = google_search(name)
      if song_name!='nothin':
       print "opening gaana to play your songs.Enjoy!"
       time.sleep(1)
       driver = webdriver.Firefox().get("http://gaana.com")
       driver.find_element_by_id("keywordsearch").clear()
       driver.find_element_by_id("keywordsearch").send_keys(name)
       driver.find_element_by_id("btnsearch").click()
       time.sleep(2)
       driver.find_element_by_css_selector("#tblheader1 > tbody > tr.GridV1BG > th[name=\"checkSelected\"] > div > input[name=\"checkSelected\"]").click()
       time.sleep(1)
       driver.find_element_by_link_text("Add to Queue").click()

     driver.find_element_by_link_text("Now Playing").click()
     driver.find_element_by_css_selector("div.checkbx > input[name=\"chk\"]").click()
     driver.find_element_by_xpath("//div[@id='mainPlayer']/div[3]/div[2]/div[6]/a").click()
    

    elif choice == 'L':
     fb_access()
    else:
     print "wrong option, please try again."
     main()

def google_search(name):
    print 'searching...'
    for url in search('%s gaana' %name, stop=1):
     if re.search(ur'http://gaana.com', url, re.UNICODE):
      return name 
     else:
      return 'nothing'


def fb_access():
    """ logs into Facebook account and asks for permission.
 Further the music names are extracted from the profile"""
   
    fbconsole.AUTH_SCOPE = ['user_likes','publish_checkins' ]
    fbconsole.authenticate()
    music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
    music_names(music)
    fbconsole.logout()


def music_names(music):
    """the music names are then checked on google
 for a valid url, which is then feeded into gaana.com"""
    music_list = music[0].values()
    for name in music_list:	#fetch music names
     music_name = (choice(name.split(','))).encode('utf-8')
     search = google_search(music_name)
     print "please wait while we search for your entries.."
     if search!= 'nothing':
       option = raw_input('now playing %s, N-> for next song; Press Y-> play; Q--> quit :' %search) #user options
       if option == 'N':
        music_names(music)
       elif option == 'Y':
        webdriver.Firefox().get(url)     #evoking gaana.com
       elif option =='Q':
        sys.exit(0)		
       else:
         print "wrong option,please try again."
         music_names(music)		
     else:
       option= raw_input( "your like doesn't match any song. N-> for next song; Q--> quit: ")
       if option == 'N':
        music_names(music)
       elif option == 'Q':
	sys.exit(0)
       else: 
        print "wrong option,please try again."
        music_names(music)
          

if __name__=='__main__':
 main()
 
