# importing the sys module that allows for arguments to be received from the command line.
from sys import argv
# setting variables for the input arguments
script, filename = argv
# opening the sample file and storing it to the variable txt.
txt = open(filename)
# commanding the program to perform the read() function on the txt variable.
# It reads out the contents of the file that was stored to the variable. 
print "Here's your file %r:" % filename
print txt.read()
txt.seek(0)			# .seek was just a test, it searches doc for 0th bit.
print txt.read(1)
txt.close()

# retreiving an input from the user that should be a file name
print "Type the file name again:"
file_again = raw_input('>')
# opening the file and storing it to a new variable.
txt_again = open(file_again)
# printing that stored text.
print txt_again.read()
txt.close()
