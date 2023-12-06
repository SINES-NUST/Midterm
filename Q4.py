#Part 1
DNA_Seq is a list of DNA sequences
G is equal to guanine in DNA_Seq
C is equal to cytosine in DNA_Seq
SET GC_content is equal to percentage 
percentage is equal to (G+C)/len(DNA_Seq)*100

#Part 2
SET x is equal to longest sequence in DNA_Seq
    FOR sequence in DNA_Seq
        IF sequence is greater than x
            print Longest sequence
        break