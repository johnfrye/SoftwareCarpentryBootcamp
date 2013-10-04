import sys

# Get the sequence
seq = sys.argv[1]
#print seq

# Create bases dictionary
bases = {}
bases['A'] = 0
bases['C'] = 0
bases['T'] = 0
bases['G'] = 0

# Loop over chars and count in dictionary
for b in str(seq):
	#print b
	if b == 'U':
		b = 'T'
	bases[b] += 1
print bases

# Calculate CG content
cgCount = bases['C'] + bases['G']
atCount = bases['A'] + bases['T']
#print cgCount
#print atCount
cgContent = cgCount * 1.0 / (cgCount + atCount)
print cgContent
