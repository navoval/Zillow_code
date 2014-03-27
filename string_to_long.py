__author__ = 'changyunglin'

# Question1: Given a string, write a routine that converts the string to a long,
#            without using the built in functions that would do this.
# Answer: We take input and put in list, and use index to access each character.
#         Since we want to change character into decimal, we read a character each time.
#         We multiply previous number by 10 and add a new character in to create digit number



def stringToLong(string):
    l = [string]
    previous = 0
    for i in range(len(l[0])):
        new = int(l[0][i])
        previous =  previous * 10 + new
    return previous


# Test section

# use self build function
string = '123456789104124323'
print "Original string: ", string
print "Original string type: ", type(string)

print 'Value of string:', stringToLong(string=string)
print 'Type of string:', type(stringToLong(string=string))

# use buildin function
print "Use build in function changing string char into decimal ", long(string, 10)

# OUT PUT:

# Original string:  123456789104124323
# Original string type:  <type 'str'>
# value of string: 123456789104124323
# type of string: <type 'int'>
# Use build in function to change string char into decimal  123456789104124323