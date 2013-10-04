import sys

fastaPath = sys.argv[1]

fastaFile = open(fastaPath, "r")
fastaLines = fastaFile.readlines()
fastaFile.close()

humanCount = 0
for line in fastaLines:
	if len(line) != 0:
		if line[0] == ">" and "OS=Homo sapiens" in line:
			humanCount += 1
print humanCount
