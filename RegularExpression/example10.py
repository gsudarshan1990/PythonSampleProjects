"""

Matching the http string in the url 'http://www.python.org'
"""

import re
url='http://www.python.org'

value=re.match('http',url)
print(value)

value=re.match('https:|ftp',url)
print(value)

value=re.match('\S*://www',url)
print(value)
