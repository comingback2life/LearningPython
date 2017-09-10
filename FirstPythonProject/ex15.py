from sys import argv
script,file_name = argv
file_name=open(file_name)
print "Here is your file %r",file_name
print file_name.read()

print "Type the file name again"
file_again=raw_input(">")
txt_again= open(file_again)

print txt_again.read()
txt_again.close()
file_name.close()




