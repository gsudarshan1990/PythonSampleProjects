"""
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.

for the text mbox-short.txt

X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000

"""

import re
filename=input('Enter the file name')

try:
    filehandle=open(filename)
except IOError as argument:
    print('Could not open the error')
    print(argument)
    exit(0)

for line in filehandle:
    line=line.rstrip()
    if re.search('^X\S*: [0-9.]+',line):
        print(line)
