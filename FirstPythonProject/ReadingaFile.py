#Reading a file in Python
from sys import argv
script, file_name= argv
print "Now I am going to read the file created in ex16.py"
target=open(file_name,'r')
print(target.read())
target.close()
