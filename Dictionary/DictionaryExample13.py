"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

filename=input('Enter the filename')

try:
    filehandle=open(filename)
except:
    print('your have entered the wrong file name')
    exit()
counts=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    if len(words)<3:
        continue
    if not line.startswith('From'):
        continue

    domain_name=words[1].split('@')
    counts[domain_name[1]]=counts.get(domain_name[1],0)+1

print(counts)

