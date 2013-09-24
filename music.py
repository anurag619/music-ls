#!/usr/bin/env python

import re
import webbrowser
import sys
import fbconsole
from google import search
from random import choice

def main():
    try:
        fbconsole.AUTH_SCOPE = ['user_likes','publish_checkins' ]
        fbconsole.authenticate()
        music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
        music_names(music)
        fbconsole.logout()
    except:
        print "some error occured in your network, please try again after some time."
        

def music_names(music):
   music_list = music[0].values()
   for name in music_list:
    music_name = (choice(name.split(','))).encode('utf-8')
    for url in search('%s gaana' %music_name, stop=1):
      if re.search(ur'http://gaana.com', url, re.UNICODE):
	      option = raw_input('now playing %s, N-> for next song; Press Y-> play :' %music_name)
	      if option == 'N':
	          music_names(music)
	      else:
	          webbrowser.open_new_tab(url)
      else:
          option1= raw_input( "your like doesn't match any song. N-> for next song: ")
	  if option1 == 'N':
	      music_names(music)
          return

if __name__=='__main__':
 main()
 sys.exit(0)
 




