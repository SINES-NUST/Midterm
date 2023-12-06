DEFINE GC_conent(sequence)
Initialize sum=0
For seq in sequence
    If seq is equal to G or C
        sum++
now initialize gc_percent= (sum/len(sequence))*100
RETURN gc_percent

DEFINE longest_seq(*lists)
Initialize max as an empty list
Initialize length=len(*list)
Append element of length to max[]
for i from 0 to length of max
    for j from i+1 to length of max
        if max[i] is greater than max[j]
            swap max[i] and max[j]
long_seq=max[0]            
RETURN long_seq