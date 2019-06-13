try:
    fh=open('C:/Users/EP833WG/Desktop/python_read_files/exceptionexample.txt','w')
    fh.write('This file has some contents written to it')
except IOError:
    print('Cannot open the file')
else:
    print('File has been written successfully')
