from sys import argv

script,file_name=argv

filehandle=open(file_name,'w')
line1=input('Enter the first line')
line2=input('Enter the second  line')
line3=input('Enter the third line')
filehandle.write(line1)
filehandle.write('\n')
filehandle.write(line2)
filehandle.write('\n')
filehandle.write(line3)
filehandle.write('\n')
filehandle.close()
