with open('C:/Users/EP833WG/Desktop/python_read_files/samplefile.txt') as fileObject:
    print('checking to see file is closed {}'.format(fileObject.closed))
    print(fileObject.read())
print('File has been read')
print('Checking to see the file is automatically closed {}'.format(fileObject.closed))
