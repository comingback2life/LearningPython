
def print_two(*args):
    arg1 , arg2 = args
    print "arg1: %r and arg2: %r"%(arg1,arg2)

def print_two_again(arg1,arg2):
    print"arg1: %r and arg2: %r"% (arg1,arg2)

def print_one(arg1):
    print("arg1: %r")%arg1

def print_none():
    print "I got nothin' Jon Snow!"

def print_infinte(*args):
    args1, args2, arg3, args4 = args
    print ("%r will %r will %r %r")%(args1,args2,arg3,args4)


print_two("Samip","Pokharel")
print_two_again("Samip Bahadur","Pokharel")
print_one("Samip")
print_none()
print print_infinte("We","We","Rock","You")


