import sys

try:
    with open('C:/Users/EP833WG/Desktop/python_read_files/samplefile2.txt') as fileobject:
        for line in fileobject:
             print(line)
except:
        print('could not open the file')
        sys.exit(1)

