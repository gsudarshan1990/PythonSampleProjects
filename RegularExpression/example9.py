"""
split the below string
'asdf fjdk; afed, fjek,asdf,      foo'
"""

import re

string1='asdf fjdk; afed, fjek,asdf,      foo'

list1=re.split(r'[;,\s]\s*',string1)
print(list1)
