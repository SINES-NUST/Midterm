#load file containing the DNA sequence
sequence=  Load file containing the sequence
length_of_seq= length of the sequence
num_GC= 0 #set GC number to 0
for i in range sequence:
    if sequence == "G" or sequence == "C":
        num_GC= num_GC+1
    End if
End for
#calculate GC content using num_GC
GC_cont= (num_GC/length_of_seq)*100
#output results
print The GC content of the sequence is:  GC_cont