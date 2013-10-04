import sys

integer = int(sys.argv[1])

if integer == 0:
	print "Zero"
elif  integer > 0 and integer < 50:
	print "Minor"
elif integer >= 50 and integer < 1000:
	print "Major"
else:
	print "Severe"
