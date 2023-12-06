#Question4
#In a bioinformatics lab, students are working with DNA sequences. They have a list of DNA sequences
#and need to perform the following tasks:
#Step 1: Calculate GC content of a DNA sequence. The GC content is the perecentage of the 
#sequence that is made up of either guanine (G) or cytosine (C) nucleotides.

dna_seq = [(DNA sequences)]
dna_length = int(len(dna_seq[0:]))
dna_g = int(dna_seq.count("G"))
dna_c = int(dna_seq.count("C"))
dna_gc = dna_g + dna_c
dna_gc_content = dna_gc/dna_length
print(dna_gc_content)

#Step 2: Find the longest sequence from a list of sequences.

dna_seq = [(DNA sequences)]
length = len(dna_seq)
list_length = list(length)
max_val = list_length.max()
print(max_val)