list_of_expenses = [15, 10, 30]
list_of_categories = ["Food", "Travel", "Entertainment"]
Food = []
Transport = []
Entertainment = []
def my_expense(expense, category):
  while category == "Food":
    return Food += expense
  while category == "Transport":
    return Transport += expense
  while category == "Entertainment":
    return Entertainment += expense
my_expense(expense = list_of_expenses, category = list_of_categories)