''''In a bioinformatics lab, students are working with DNA sequences. They have a list of DNA sequences
and need to perform the following tasks:'''

'''STEP 1: Calculate GC content of a DNA sequence.The GC content of a DNA sequence is given by the 
percentage of the sequence that is made up of either guainine (G) or cytosine (C) nucleotides.'''

DNASequence = ["list of DNA sequence"]
DNASequence.count("G","C")
GC = DNASequence.count("G","C")
GCcontent = GC divide by len(DNASequence) multiply by 100

GCcontent = %
print(GCcontent)
output will give the % of GC content

'''STEP 2: Find the Longest Sequence from  a list of sequnces'''
longest sequence from a list of sequences: suppose we have 4 lists of DNA sequences of different lengths

List1 = [DNASequence]
List2 = [DNASequence]
List3 = [DNASequence]
List4 = [DNASequence]

a = len(List1)
b = len(List2)
c = len(List3)
d = len(List4)

if a>b+c+d:
    print("List1 is the longest sequence")
elif b>a+c+d:
    print("List2 is the longest sequence")
elif c>a+b+d:
    print("List3 is the longest sequence")
elif d>a+b+c:
    print("List4 is the longest sequence")
else:
    print("none has greater/longest sequence")
    
or we can compare 2 sequences of DNA:

list1 = [DNASequence]
list2 = [DNASequence]

a = len(list1)
b = len(list2)

if a>b:
    print("list1 is the longest sequence")
elif b>a:
    print("list2 is the longest sequence")
else:
    print("both lists are equal in length")