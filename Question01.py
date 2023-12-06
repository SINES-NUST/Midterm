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
  