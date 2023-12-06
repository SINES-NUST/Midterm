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
  