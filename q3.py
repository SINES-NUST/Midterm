DEFINE category(list_of_expenses)
Initialize a empty list as FOOD_category
Initialize a empty list as TRANSPORT_category
Initialize a empty list as ENTERTAINMENT_category
set list_of_expenses as a input variable
set_Food=["groceries","tea,"dinners","lunches","snacks","breakfast","coffee"]
set_Transport=["bus","train","taxi","flight"]
set_Entertainment=["movies","games","books","magazines","music"]
for items in list_of_expenses:
    if items in set_Food:
        FOOD_category.append(items)
            print the food category items
    elif items in set_Transport:
        TRANSPORT_category.append(items)
            print the transport category items
    elif items in set_Entertainment:
        ENTERTAINMENT_category.append(items)
            print the entertainment category items
return(FOOD_category,TRANSPORT_category,ENTERTAINMENT_category)