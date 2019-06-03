from sys import argv

script, file_name=argv

filehandle=open(file_name,'w')
filehandle.truncate(0)
filehandle.close()
