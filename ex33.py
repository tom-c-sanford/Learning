def while_practice(count, increm):

	i = 0 
	numbers = []


	for i in count:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i+increm
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

while_practice(range(0, 6), 1)