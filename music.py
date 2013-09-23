
import fbconsole
from random import choice
import re
import webbrowser
from google import search
import sys


def main():
 try:
  fbconsole.AUTH_SCOPE = ['user_likes' ]	#fbconsole authentication
   fbconsole.authenticate()
   music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
   music_names(music)

   except:		#handling HTTP errors
    print "some error occured in your network, please try again after some time."
        

def music_names(music):		#parsing the music names
   music_list = music[0].values()
   for name in music_list:
    music_name = (choice(name.split(','))).encode('utf-8')
    for url in search('%s gaana' %music_name, stop=1):		#searching for the names in gaana.com
      if re.search(ur'http://gaana.com', url, re.UNICODE):
	option = raw_input('now playing %s, N-> for next song; Press Y-> play :' %music_name) #user options
	if option == 'N':
	 music_names(music)
	else:
	 webbrowser.open_new_tab(url)
      else:
        print "your like doesn't match any song. N-> for next song: "
	break
    break
	

if __name__=='__main__':
 main()
 sys.exit(0)
 




