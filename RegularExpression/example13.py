"""

Matching digits
text1 = '11/27/2012'
 text2 = 'Nov 27, 2012'
"""
import re
text1='11/27/2012'
day=re.findall('^\d+',text1)
print(day)

if re.match('\d+/\d+/\d+',text1):
    print("Date Matched")

text2 ='Nov 27, 2012'

if re.match('\S* \d+, \d+',text2):
    print('Second Date Matched')

month=re.findall('^\S*',text2)
print(month)

text3='Today is 11/27/2012. PyCon starts 3/13/2013.'

dates=re.findall('\d+/\d+/\d+',text3)
for date in dates:
    print(date)


