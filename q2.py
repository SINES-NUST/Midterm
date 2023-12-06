Start 
Display List_1 # List_1 consists of name, sales and amount earned by employee.
Assume the threshold of average is equal to 50.
x=average above 50
y=average below 50
# First we will find the average.
# For this we will make a function.
Define a funtion named average_sales (infinity)
    average= sum of sales/total sales
    print ("name of employee", amount earned, average)
# We will find the averages of all the employees by the mentioned function and stored it in a list_universal.
# we will make two lists in which the employees having more than average sales and less averages will be kept.
Display List_2 # High (acceptable averages)
Display List_3 # Low (less averages)
For items in list_universal
    if items is less than or equal to y
        Then store it in list_3
    ELSE items equal to x
        Then store it in list_2
Print (List_2) # Display the employees having more than average sales.
Print (List_3) # Display the employees having less than average sales.
END 