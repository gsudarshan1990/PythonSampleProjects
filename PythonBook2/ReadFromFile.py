from sys import argv

script, file_name=argv

print(f'the file name is {file_name}')
filehandle=open(file_name)
print(filehandle.read())
filehandle.close()

filename=input('enter the file name')
filehandle=open(file_name)
print(filehandle.read())
filehandle.close()
