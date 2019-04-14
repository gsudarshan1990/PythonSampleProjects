i=0
with open('C:/Users/EP833WG/Desktop/python_read_files/FileExercise1.txt') as fileObject:
    for line in fileObject:
        i=i+1
        print(str(i)+':'+' '+line)
