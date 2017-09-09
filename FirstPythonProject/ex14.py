'Combining argv and raw_input'
from sys import argv
script,user_name = argv
prompt=">"
print "Hi %s I am the %s"%(user_name,script)
print "I would like to ask you a few questions"
print "Do you like me?"
likes=raw_input(prompt)

print "Where do you live?"
address=raw_input(prompt)

print "What kind of computer do you have ?"
computer=raw_input(prompt)

print """
Alright So, you said %r about liking me
You live in %r. Not sure where it is.
You have a %r computer. Nice.
"""%(likes,address,computer)

