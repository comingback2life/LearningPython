def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %r cheeses!"%(cheese_count)
    print "You have %r boxes of crackers"%boxes_of_crackers
    print "That is enough for a party"
    print "Get your blanket now. \n"

print "We can give the numbers directly:"
cheese_and_crackers(30,20)

print "Or we can give values from variables from the script"
amount_of_cheese=10
amount_of_crackers=30
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "Let's do a math inside it then"
cheese_and_crackers(20+30, 40+40)

print" and lastly, we can combine two variables and do the math"
cheese_and_crackers(amount_of_cheese+10,amount_of_crackers+20)

print "Can we assign values to arguments from a function?"
cheese_and_crackers(cheese_count=10 , boxes_of_crackers=33)
