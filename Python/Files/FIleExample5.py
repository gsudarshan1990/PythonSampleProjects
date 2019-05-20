"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

"""
import math

fname=input('Enter the file name')
filehandle=open(fname)
count=0
list_values=[]
sum=0
for line in filehandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count+=1
        line=line.rstrip()
        line_word=line.split()
        list_values.append(float(line_word[1]))
for element in list_values:
        sum=sum+element
average=sum/count
print(average)
