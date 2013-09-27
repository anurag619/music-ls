#!/usr/bin/env python

import re
import webbrowser
import fbconsole
from google import search
from random import choice

def main():
	""" logs into Facebook account and asks for required permission. Further the music names are extracted from the profile"""
    try:
        fbconsole.AUTH_SCOPE = ['user_likes','publish_checkins' ]
        fbconsole.authenticate()
        music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
        music_names(music)
        fbconsole.logout()
    except:
        print "some error occured in your network, please try again after some time."
        

def music_names(music):
	"""the music names are then checked on the google for a valid url, which is then feeded into gaana.com"""
	
   music_list = music[0].values()
   for name in music_list:		#fetch music names
    music_name = (choice(name.split(',')),int(len())).encode('utf-8')
    for url in search('%s gaana' %music_name, stop=1):
      if re.search(ur'http://gaana.com', url, re.UNICODE):
	      option = raw_input('now playing %s, N-> for next song; Press Y-> play :' %music_name) #user options
	      if option == 'N':
	          music_names(music)
	      else:
	          webbrowser.open_new_tab(url)		#evoking gaana.com
      else:
          option1= raw_input( "your like doesn't match any song. N-> for next song: ")
	  if option1 == 'N':
	      music_names(music)
          

if __name__=='__main__':
 main()
 
