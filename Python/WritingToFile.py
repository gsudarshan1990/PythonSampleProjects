with open('C:/Users/EP833WG/Desktop/python_read_files/newfile.txt','w') as fileObject:
    fileObject.write('This is the second file.\n')
    fileObject.write('I have written some contents on the second file')

with open('C:/Users/EP833WG/Desktop/python_read_files/newfile.txt') as fileObject:
    for line in fileObject:
        print(line)


with open('C:/Users/EP833WG/Desktop/python_read_files/newfile.txt','a') as fileObject:
    fileObject.write('I have written this statement after opening the file in the append mode')

with open('C:/Users/EP833WG/Desktop/python_read_files/newfile.txt') as fileObject:
    for line in fileObject:
        print(line)


try:
    open('C:/Users/EP833WG/Desktop/python_read_files/n.txt')
except:
    print('no file exists')
