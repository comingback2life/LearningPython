'The program uses import statements'

script=raw_input("Enter the Script name")
first=raw_input("Enter the first variable name")
second=raw_input("Enter the second variable name")
third=raw_input("Enter the third variable name")

from sys import argv

script, first, second, third = argv
print "The Script is ",script
print "The first variable is ",first        
print "The second variable is",second
print "The third variable is",third
