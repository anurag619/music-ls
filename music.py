
import fbconsole
from random import choice
import re
import webbrowser
from google import search

fbconsole.AUTH_SCOPE = ['user_likes' ]
fbconsole.authenticate()
q = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
s = q[0].values()
for name in s:
 n = (choice(name.split(','))).encode('utf-8')
 for url in search('%s gaana' %n, stop=1):
      if re.search(ur'http://gaana.com', url, re.UNICODE):
	webbrowser.open_new_tab(url)
	break
 break
 




