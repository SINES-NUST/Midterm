#initialize variables
Tot_books = input What is the total number of books?
Change type of Tot_books to integer
#initialize lists
fiction= []
nonfiction= []
#input each book's name and ask if  it is fiction or not
for eachbook in range (Tot_books):
    book_name= input book's name
    fic_or_not= input Is the book fiction
    if fic_or_not == "yes":
        Append book_name to fiction
    else:
        Append book_name to nonfiction
End for
#output results
print Fiction books are:  fiction
print Nonfiction books are:  nonfiction