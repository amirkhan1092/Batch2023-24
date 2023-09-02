# web user id and password

import urllib.request
import urllib.parse

url = 'http://localhost:8080/cgi-bin/web_user.py'
values = {'name' : 'Michael Foord',
            'location' : 'Northampton',
            'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)

