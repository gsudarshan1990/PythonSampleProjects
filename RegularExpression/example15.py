"""

Usage of Escape Character
"""
import re
x = 'We just received $10.00 for cookies.'
result=re.findall('\$[0-9]+\.[0-9]+',x)
print(result)
