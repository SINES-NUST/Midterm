#intialize variables to identify lower sales and average sales and list of employees
Average_sale = 10
Lower_sale = 1
employee_list = [ "Employee 1", "Employee 2", "Employee 3","Employee 04"]
#iterate through the employee_list to check sales of each employee
#calculate sales of each employee to cehck sales
total_sale = sum(employee.sales)
#update list after intializing a list of employee sales
employee_sales=[]
#Now update employee sales
if total_sale > Lower_sale:
    Lower_sale=Average_sale
    Average_salesman=employee
#iterate through all employee list
#Return results or display results
print("Employee with average sales", Average_salesman.name, "with total sales of", Average_sale)
print("Employee with lower sales", Lower_salesman.name, "with total sales of", Lower_sale)