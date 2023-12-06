set range to n
set my_fiction to an empty list []
set my_nonfiction to an empty list []
for i in range:
  enter book_name from user
  enter book_type from user
  if book_type == fiction:
    my_fiction=book_name
  else:
    my_nonfiction=book_name
  continue
#user input of n which is range
n= "enter range of books"
write my_fiction #list of fiction books
write my_nonfiction #list of nonfiction books