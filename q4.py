start 
dispaly list_DNA # List of DNA sequences.
Step 1:
# Suppose we have three sequences in the list_DNA , each is present as a separate string.
List_DNA at index [0] = x
List_DNA at index [1] = y # y consists of second sequence.
List_DNA at index [2] = z # z consists of third sequence.
let cytosine = C
let guanine = G
# we will make three lists
List_1 # GC content of first sequence.
List_2 # GC content of second sequence.
List_3 # GC content of third sequence.
For items in x
    if items is equal to C and G
        add it to list_1
For items in y
    if items is equal to C and G
        add it to list_2
For items in z
    if items is equal to C and G
        add it to list_3
# Now we will make a function to find the actual number of GC content.
Define  calculate_GC (infinity)
    number of GC = sum of all GC
    print (sum of GC)
# By using the funtion, we can find the sum of GC.
END 
Step2:	
Start 
Display list_DNA # List of DNA sequences.
Longest sequence = x
For items in list_DNA
    IF items is equal to x
        print ("longest DNA", sequence)
    ELSE items is not equal to x
        print ("shortest DNA", sequence)
END
