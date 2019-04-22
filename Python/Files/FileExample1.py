

file_object = open("C:\\Users\\EP833WG\\Desktop\\python_read_files\\test.txt")
s1=file_object.read()
print(s1)
print('*'*20)
s2=file_object.read()
print(s2)
print('*'*20)
file_object.seek(0)
s3=file_object.read()
print(s3)
file_object.seek(0)
print('read lines')
list= file_object.readlines()
print(list)

file_object.close()

print('*'*20+'reading using with'+'*'*20)
with open("C:\\Users\\EP833WG\\Desktop\\python_read_files\\test.txt",'r+') as file_object2:
    file_object2.write('\nthis is the fourth line')
    print(file_object2.read())

