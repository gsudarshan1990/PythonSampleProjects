fileobject=open('C:/Users/EP833WG/Desktop/python_read_files/samplefile.txt')
print('Current Position {}'.format(fileobject.tell()))
print(fileobject.read())

print('current position {}'.format(fileobject.tell()))
data=fileobject.read()
if not data:
    print('-'*20)
    print('file is at last position hence no data')
    print('#'*20)
else:
    print(data)

fileobject.seek(5)
print('current poistion {}'.format(fileobject.tell()))
print(fileobject.read())


fileobject.seek(0)
print(fileobject.read(17))
print(fileobject.tell())

print('is the file close {}'.format(fileobject.closed))

if not fileobject.closed:
    fileobject.close()

print('is the file closed {}'.format(fileobject.closed))
