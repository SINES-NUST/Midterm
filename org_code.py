#Question:1
list_of_books = ["A", "B", "C", "D"]
category_list = ["Fiction", "Non-Fiction", "Fiction", "Fiction"]
index_of_fiction = []
index_of_nf = []
for category in category_list:
  if category == "Fiction":
    index_F = category_list.index(category)
    index_of_fiction += index_F
  else:
    index_of_nf = category_list.index(category)
fiction_books = []
nonfiction_books = []
for book in list_of_books:
  index_books = list_of_books.index[book]
  if index_books == index_of_fiction:
    fiction_books+=book
  elif index_books == index_of_nf:
    nonfiction_books+=book

#Question:2
names = ['A', 'B', 'C']
sales = [10, 8, 9]
target = [10, 6, 15]

#find the average sales
sum = 0
for s in sales:
  sum = sum + s
number = 0
for n in sales:
  number = number + 1
average_sales = sum/number
index_sales = []
for s in sales:
    if s < average_sales:
        index_sales += sales.index(s)
        index_sales+=index_sales
    else:
      continue
employees_below_avg = []
for name in names:
  index_name = names.index(name)
  if index_name == index_sales:
    employees_below_avg += name
  else:
    continue
  
#Question: 3
list_of_expenses = [15, 10, 30]
list_of_categories = ["Food", "Travel", "Entertainment"]
Food = []
Transport = []
Entertainment = []
def my_expense(expense, category):
  while category == "Food":
    return Food += expense
  while category == "Transport":
    return Transport += expense
  while category == "Entertainment":
    return Entertainment += expense
my_expense(expense = list_of_expenses, category = list_of_categories)

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