from dna_sequence import DNASequence
import sys


seq = sys.argv[1]


mySeq = DNASequence(seq)
print mySeq.base_count('A')
print mySeq.gc_content()
print mySeq.reverse_complement()
