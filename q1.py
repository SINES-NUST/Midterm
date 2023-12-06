DEFINE organize(books)
Initialize fiction_list
Initialize nonfiction_list
set fiction as an empty list
set nonfiction as an empty list
for i from 0 to length of books
    if books[i] is present in fiction
        fiction.append (books)
    print fiction
    else
        nonfiction.append (books)
    print nonfiction
Return fiction,nonfiction