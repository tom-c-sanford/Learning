from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening the file..."

print "Now I'm going to ask you for three lines."

line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ')
line3 = raw_input('line 3: ')

with open(filename, 'r+') as f:
	print "I'm going to write these to the file."
	f.truncate()
	f.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
	f.seek(0)
	print "Now I'll print out the file's new contents:"
	print f.read()
