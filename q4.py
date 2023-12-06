part A 
initialize variable 'dna' to store DNA sequence and variables count=0 and percentage=0
iterate through the length of 'dna':
    if 'dna' at specific position=='G' or 'C'
        count++
    return count
end Loop

percentage = (count/len(dna))*100
print ("GC count is:", percentage)

part B 
take list of sequences from user as 'dna1', 'dna2', and 'dna3' such as 
dna1= ['ATGCGATACGATCGAGGGCCAT']
dna2= ['ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT']
dna3= ['ACTGACACACTGTAGTAGTA']

compare all three to find sequence with longest length. 
if dna1(len)>dna2(len) and dna1(len)>dna3(len)
    print ("longest seq is dna1: ", dna1)
else if dna2(len)>dna1(len) and dna2(len)>dna3(len)
    print ("longest sequence is dna2: ", dna2)
else
    print ("longest sequence is dna3: ", dna3)
    