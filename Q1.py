List=['a',1,2,3,'b','c','d',4,5]
fiction_books=[i for i in List if i==int]
non_fiction_books=[j for j in List if j=='str']
print(fiction_books)
print(non_fiction_books)