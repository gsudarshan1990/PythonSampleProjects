with open('C:/Users/EP833WG/Desktop/python_read_files/samplefile.txt') as fileobject:
    for line in fileobject:
        print(line)

print('Removing the carriage return')

with open('C:/Users/EP833WG/Desktop/python_read_files/samplefile.txt') as fileobject:
    for line in fileobject:
        print(line.rstrip())

print('is the file closed {}'.format(fileobject.closed))

print(fileobject.mode)
