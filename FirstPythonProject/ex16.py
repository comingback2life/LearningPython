from sys import argv
script, file_name = argv

print " We are going to create a file %r",file_name
print "If you do not want that please press Ctrl+C"
print "If you do want that hit return"
raw_input("?")
print "Opening the file...."
target=open(file_name,'w') #w is for write method
print "Truncating the file, Goodbye!"
target.truncate()
print "Now I am going to ask you for three things"
line1=raw_input("Line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "Now I am going to write all the lines into the text file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And we are finally going to close the file")
target.close()

