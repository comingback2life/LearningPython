#This program is from ex6 of Zed A. Shaw : Learning python the hard way!
x="There are %d kinds of people" %10
binary= "binary"
do_not = "don't"
y= "Those who know %s and those who %s know binary" %(binary,do_not)
print x
print y

print "I also said %r" %x
print "And I also said %s" %y

hilarious = False
joke_evaluation = "Isn't that joke so funny ? %r"
print joke_evaluation % hilarious

w="This is the left side of..."
e= "a string with a right side"
print w+e

