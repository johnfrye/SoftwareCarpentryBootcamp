import sys
from rodents import Rodent

rodPath = sys.argv[1]

#rodFile = open(rodPath, "r")
#rodLines = rodFile.readlines()

#rodFile.close()

rodents = {}

rodFile = open(rodPath)

for line in rodFile:
	if len(line) > 0:
		l = line.split(',')
		newTag = l[0]
		newWeight = l[1]
		
		# Check if already in dict
		if newTag not in rodents:
			rodents[newTag] = Rodent(newTag)
			rodents[newTag].add_weight(newWeight)
		else:
			rodents[newTag].add_weight(newWeight)

rodFile.close()

for key in rodents:
	r = rodents[key]
	print r.tag_id, r.weights
