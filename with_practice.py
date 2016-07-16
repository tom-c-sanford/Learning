from sys import argv

script, filename = argv

#open up the file and write to/read it. Use the with statement to automatically close.
with open(filename, 'r+') as f:
	print f.read()
	f.write("This is a cool test of the with command. \nGive it a shot! \nSee if it will write and read this thing")
	f.seek(0)
	print f.read()

#with open(filename) as f:
#	print f.read()

