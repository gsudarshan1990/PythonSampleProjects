"""
Transfer of contents from one file to another
"""

from sys import argv
from os.path import exists

script, in_file, out_file=argv

in_file_split=in_file.split('/')
in_file_name=in_file_split[len(in_file_split)-1]
out_file_split=out_file.split('/')
out_file_name=out_file_split[len(out_file_split)-1]
print(f'Data is transferred from {in_file_name} to {out_file_name}')

in_filehandle=open(in_file)
data=in_filehandle.read()

print('Check whether the out put file exists',exists(out_file))
out_filehandle=open(out_file,'w')
out_filehandle.write(data)

in_filehandle.close()
out_filehandle.close()
