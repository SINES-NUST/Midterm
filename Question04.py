#Question: 4
sequences = ['ACGAT', 'GAACCT']
length_of_seq = []
for s in sequences:
  C_content = s.len('C')
  G_content = s.len('G')
  total_length = len(s)
  length_of_seq += total_length
  total_percentage_C = (C_content/total_length)*100
  total_percentage_G = (G_content/total_length)*100
  GC_content = total_percentage_C + total_percentage_G
len_longest_sequence = 0
for seq in sequences:
  if len(seq) > len_longest_sequence:
    len_longest_sequence = len(seq)
    longest_sequence = seq
print(f"The longest sequence is {longest_sequence}")