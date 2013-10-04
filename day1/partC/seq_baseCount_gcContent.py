
import sys

seq = sys.argv[1]

def base_count(seq, base):
	count = seq.count(base)
	return count

def gc_content(seq):
	bases = {}
	bases['A'] = 0
	bases['C'] = 0
	bases['T'] = 0
	bases['G'] = 0
	
	for b in seq:
		bases[b] += 1

	at = bases['A'] + bases['T']
	cg = bases['C'] + bases['G']

	content = cg * 1.0 / (at + cg)
	
	return content

"""
# SOLUTION
def base_count(sequence, base):
    return sequence.count(base)
    
def gc_content(sequence):
    return (base_count(sequence, 'G') + 
            base_count(sequence, 'C')) / float(len(sequence))
"""


print base_count(seq, 'A')

print gc_content(seq)
