#Excercise 17 -
from sys import argv
from os.path import exists
script, file_to, file_from = argv
print "Copying file from %s to %s"%(file_to,file_from)
in_file=open(file_from)
indata=in_file.read()

print "The file is %r characters long"%len(indata)
print"Does the file we are trying to copy to exists ?%r"%exists(file_to)
print "Hit Enter to Continue or press Ctrl+C to abort copying "
raw_input()
copyinfile=open(file_to,'w')
copyinfile.write(indata)
print "The file has been written. Congratulations !"
in_file.close()
copyinfile.close()
