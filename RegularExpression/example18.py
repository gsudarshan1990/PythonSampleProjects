"""
Usage of Sub function of regular expression for replacement

"""
#Replacing the String
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
result=re.findall('python',text,flags=re.IGNORECASE)
print(result)
print('Substitue Python with Snake')
result=re.sub('python','snake',text,flags=re.IGNORECASE)
print(result)

text= 'Every DC Movies are great movies'
result=re.sub('DC','Marvel',text)
print(result)


text='Every DC Movies are great Movies!! Really great Movies'
result=re.sub('Movies','Cartoons',text)
print(result)

#Replace the format of the Date
text='Today is 11/27/2012. PyCon starts 3/13/2013.'
result=re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
print(result)


