class DNASequence:
	def __init__(self, seq):
		self.seq = seq
		self.base_counts = {}

	def base_count(self, base):
		if base in self.base_counts:
			return self.base_counts[base]
		else:
			count = self.seq.count(base)
			self.base_counts[base] = count
			return count

	def gc_content(self):
		g = self.base_count('G')
		c = self.base_count('C')
		#print g
		#print c
		#print len(self.seq)
		return (g + c) * 1.0 / len(self.seq)

	def reverse_complement(self):
		rev = self.seq[::-1]
		newSeq = ""
		for char in rev:
			if char == "A":
				newSeq += "T"
			elif char == "T":
				newSeq += "A"
			elif char == "C":
				newSeq += "G"
			elif char == "G":
				newSeq += "C"
		return newSeq


