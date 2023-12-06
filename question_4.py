assumption = mona has 2 lists:
books = []
tags = [] 
tags 'f' for fiction, 'nf' for non-fiction 

1- creating a list called books
2- creating a list called tags
3- creating a loop 
for ith element in books:
    if ith entry in tags == 'f':
        print("book name classified as fiction:", ith element)
        store ith element in list called fictional_books
    elif ith entry in tags == 'nf':  
        print("book name classified as non-fiction:", ith element)
        store ith element in list called non-fictional_books
return fictional_books, non-fictional_books