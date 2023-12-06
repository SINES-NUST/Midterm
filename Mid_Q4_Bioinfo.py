'''In a bioinformatics lab, students are working with DNA sequences. They have a list of DNA sequences
and need to perform the following tasks:'''

'''STEP 1: Calculate GC content of a DNA sequence.The GC content of a DNA sequence is given by the 
percentage of the sequence that is made up of either guainine (G) or cytosine (C) nucleotides.'''

#defining function
 def GC_content(DNA_seq)
    T_bases=length(DNA_seq) #T_bases is the total number of bases in the sequence
    GCcount=0
    if T_bases==0
        return "Empty Sequence"
    for base in DNA_seq
        if base=="G" or base=="C":
            GCcount add
    GC_content=(GCcount/T_bases)*100
    return GC_content

'''STEP 2: Find the Longest Sequence from a list of sequence.'''

def maxseqlength()
   DNA_seq=List of sequnce
   for i from 1 to maxseqlength:
      if i==length(DNA_seq)
         print the value of maximum length
      else
         return the error.
