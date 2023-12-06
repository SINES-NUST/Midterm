Start 
Dispaly List_universal # it consists of all the expenses of food transport and entertainment
# he will display 3 lists, each list specific for specific expenses.
Display List_1 # for food
Display List_2 # for transport
Display List_3 # for entertainment
let x = food expenses
let y = transport expenses
let z = entertainment expenses
for items in universal list (List_universal)
    if items is equal to x
        add it to list_1
    elif items is equal to y
        store it in to list_2
    else items is equal to z
        store it in list_3
Print (List_1) # Display the food expenses.	
Print (List_2) # Display the transport expenses.
Print (List_3) # Display the entertainment expenses.
End 
