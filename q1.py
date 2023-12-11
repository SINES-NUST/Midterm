#create a list of fiction books
name it "list 1"
create a list of non-fiction books
name it "list 2"
for each book in list 1:
    if the book is not in list 2:
        add it to list 1
        for each book in list 2:
            if the book is not in list 1:
                add it to list 2
                display list 1 and list 2