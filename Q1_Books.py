#Mona has decided to organize her library into fiction and non-fiction,
#help Mona sort her library out that she has 2 separate lists for fiction and non-fiction books.

#initialize variable to store Mona's whole library in a list
LibraryList = ['...', '...', '...', etc]

#Apply for loop in the length of LibraryList and initialize each element
for i in range(0:len(LibraryList)):

#The loop will read from first element till the end (length) of LibraryList
LibraryList[i]

#Apply condition in if form
    if LibraryList[i] == "fiction":
    #if the condition is true, we will add to new list called 'FictionList'
        FictionList = LibraryList[i]
    else:
    #if the condition is not true, we will add to another list called 'NonFictionList'
        NonFictionList = LibraryList[i]
#Output both the lists to view 2 separate lists for fiction and non-fiction books
print(FictionList)
print(NonFictionList)