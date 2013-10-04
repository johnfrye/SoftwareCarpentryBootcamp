class NucleotideSequence:
    """
    This is an abstract class defining the basic
    methods for both DNA and RNA
    """
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    valid = set(complements)
    
    def __init__(self, sequence):
        """
        Input sequence should be a string in all
        upper case letters
        """ 
        try:
            assert isinstance(sequence, str)
        except AssertionError:
            raise Exception("Input not a string")

        try:
            assert len(sequence) > 0
        except AssertionError:
            raise Exception("The sequence is not long enough")

        try:
            assert set(sequence).difference(self.valid) == set()
        except AssertionError:
            raise Exception("Invalid base; bases:" + ''.join(set(sequence).difference(self.valid)))

        self.sequence = sequence
        self.base_counts = {}
    
    def base_count(self, base):
        """
        Given a base, returns the number of times the
        base occurs in this sequence.
        """
        assert isinstance(base, string) == True
        assert len(base) == 1
        assert set(base).difference(self.valid) == set()

        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        """
        Returns the G + C vs ALL BASES ratio
        Number from 0 to 1
        """
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g + c) / len(self.sequence)
        
    def reverse_complement(self):
        """
        Outputs the reverse complement of the sequence
        The reverse complement is obtained by reversing
        the sequence, and changing each base to its complement
        """
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
        
class DNASequence(NucleotideSequence):
    """
    This is the DNASequence class, it inherits from
    the NucleotideSequence class
    """
    pass
    
    
class RNASequence(NucleotideSequence):
    """
    This is the RNASequence class, it inherits from
    the NucleotideSequence class
    Create a new complement
    """
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}
    valid = set(complements)
