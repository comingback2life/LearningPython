'This program uses int(raw_input()) to carry out calculation of Simple Interest'
print "Please enter the principal",
principal=int(raw_input())
print "Please enter the rate ",
rate=float(raw_input())
print "Please enter the time ",
time= float(raw_input())
SimpleInterest = (principal*time*rate)/100
print "The principal was %s , the time was %s and the rate was %s so the Simple Interest is %s"%(principal,time,rate,SimpleInterest)