'''A sales company wants to identify employess whose sales are much lower than the average sales. 
They have a document that lists the name of the employee, the sales and the amount earned by the sales,
they also have the targets given, choose the best variable that will allow them to identify 
the requirements above.'''

Employees_data = [{"name of employee": "", "Sales":  , "targets": , "amount earned by sales"}]
data = [total amount earned by the sales]
average_sales = np.mean(data)

for i in Employees_data:
    name of employee = Employees_data["name of employee"]
    
    sales = Employees_data["sales"]
    
    if sales < average_sales:
        print("The employee"+ name of employee + "has sales" + sales + "which are lower than average")

    else:
        print("The employee"+ name of employee + "has sales" + sales + " above average")