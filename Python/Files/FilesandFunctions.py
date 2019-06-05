from sys import argv

script, file_name=argv

index_of_forwardslash=file_name.rfind('/')
file_name_without_slash=file_name[index_of_forwardslash+1:]
print('You are reading from the file name',file_name_without_slash)

def print_from_file(filehandle):
    print(filehandle.read())

def rewind(filehandle):
    filehandle.seek(0)

def print_line_by_line(linenumber,filehandle):
    print(str(linenumber)+":"+filehandle.readline())

filehandle=open(file_name)
print_from_file(filehandle)

rewind(filehandle)

line_number=1
print_line_by_line(line_number,filehandle)

next_line_number=line_number+1
print_line_by_line(next_line_number,filehandle)

next_line_number=line_number+1
print_line_by_line(next_line_number,filehandle)
