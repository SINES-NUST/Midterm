DNA_sequences=[['A','T','G','C','T','G','C'],#seq1
               ['A','T','G','C','T','G','C'],] #seq2
set seq1_count to 0
set seq2_count to 0
seq1_count= seq1.count() #first DNA seq count
seq2_count= seq2.count() #second DNA seq count
function total_GC (total_GC_cpunt):
    for i in DNA_sequences:
        if i=='G' or i=='C'in seq1:
            GC_storage=i
    GC_count=GC_storage.count()
    total_GC_count=GC_count % seq1_count * 100
    write total_GC_count
#function call
total_GC(total_GC_count)

#part two of the question

set seq1_count to 0
set seq2_count to 0
seq1_count= seq1.count() #first DNA seq count
seq2_count= seq2.count() #second DNA seq count
if seq1_count > seq2_count:
    write ("longest DNA sequence",seq1_count)

#can itterate through a loop to find the longest DNA sequence