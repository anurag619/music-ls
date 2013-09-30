#!/usr/bin/env python

import fbconsole
import re
import webbrowser
from google import search
from random import choice
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
        """ logs into Facebook account and asks for required permission. Further the music names are extracted from the profile"""
   
        fbconsole.AUTH_SCOPE = ['user_likes','publish_checkins' ]
        fbconsole.authenticate()
        music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
        music_names(music)
        fbconsole.logout()
    
        

def music_names(music):
   """the music names are then checked on the google for a valid url, which is then feeded into gaana.com"""
   
   music_list = music[0].values()
   for name in music_list:		#fetch music names
    music_name = (choice(name.split(','))).encode('utf-8')
    for url in search('%s gaana' %music_name, stop=1):
      if re.search(ur'http://gaana.com', url, re.UNICODE):
	      option = raw_input('now playing %s, N-> for next song; Press Y-> play; Q--> quit :' %music_name) #user options
	      if option == 'N':
	          music_names(music)
	      elif option == 'Y':
		   webdriver.Firefox().get(url)		#evoking gaana.com
	      else:
 	           sys.exit(0)
	         		
      else:
          option= raw_input( "your like doesn't match any song. N-> for next song; Q--> quit: ")
	  if option == 'N':
	      music_names(music)
	      sys.exit(0)
	  else: sys.exit(0)
          

if __name__=='__main__':
 main()
 
