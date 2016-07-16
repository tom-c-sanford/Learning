#This is an import - adds modules that python otherwise wouldn't include in the program
#argv holds the arguments I will pass to the script when I run it.
from sys import argv
# unpacking the argv and assgins the info to four variables
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

answer = raw_input("Are you sure those variables are correct? ")
print "So, you said that %s the variables are correct. %s, %s, %s" % (answer, first, second, third)