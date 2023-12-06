#Question 1
#Mona has decidedto organize her library into fiction and non-fiction,
#help Mona sort her library out that she has 2 separate lists for fiction and non-fiction books.

fiction = []
non_fic = []

book = input("What is the name of the book?\n")
fic = input("Is it fiction or non-fiction? Pick F for fiction and NF for nonfiction.\n")

while fic == "F" or fic == "NF":
  if fic == "F":
    fiction.append(book)
    print(fiction)
  elif fic == "NF":
    non_fic.append(book)
    print(non_fic)
  else:
    print("Please enter F or NF")
  book = input("What is the name of the book?")
  fic = input("Is it fiction or non-fiction? Pick F for fiction and NF for nonfiction.")
else:
    print("Your library has been successfully sorted!")
