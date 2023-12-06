#Question 3
#Ahmed is keeping track of his daily expenses. He wants to categorize them into "Food", "Transport",
#and "Entertainment". Write pseudo-code to loop through the list of expenses and categorize
#them into the respective categories.

expenses = [500, 100, 200, 300, 350]
Food = []
Transport = []
Entertainment = []

def categorise():
    expense = input("What is your expense?")
    category = input("Food, Transport, or Entertainment? Press F for Food, T for Transport, and E for Entertainment.")
    if category == "F":
        Food = Food.append(expense)
        print(Food)
    elif category == "T":
        Transport = Transport.append(expense)
        print(Transport)
    elif category == "E":
        Entertainment = Entertainment.append(expense)
        print(Entertainment)