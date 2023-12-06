step1: calculating GC content of DNA sequences
Assumption: We have a list of 10 DNA sequences 

1- creating a list whose name is DNA-Sequence that contains the DNA sequence students are working with. List contains string variables.
2- Finding length of each DNA sequence using a loop so:
   for i in range(10):
     creating a variable that does count = count+1 
     it adds value at ith place in another list called DNA_seq_len
     returning the variable DNA_seq_len
3- creating another for loop for GC content so:
    for sequence in DNA-seq in range 10
      if each ith element contains 'G' or 'C'
        char_count = char_count+1
        add char_count to ith place in another variable that is a list containing char_counts called GC_content
        return GC_content
4- To calculate GC percentage.
   Creating a function called perc_calc that takes two lists as arguments:
      Fucntion divides first list by second, multiplies it by 100, stores value in 3rd list
      returns 3rd list
5- calling the function perc_calc with arguments GC_content and DNA_seq_len, third list is callled GC_perc
6- print("GC content of each sequence is:", GC_perc)

step2: finding the longest sequence
1- creating a function longest_seq that takes one list as argument
      creating a variable called seq and providing it value = 0 
      creating a loop that runs through range of list 
          if ith element > seq
             seq = ith element
             print("Longest sequence is:", ith element)
             return seq 
2- calling the function longest_seq and passing our list DNA-seq. Longest sequence will be printed on screen. 