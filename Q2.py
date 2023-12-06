def lower_averageemp(Employee_data):
    #assuming game data is a list dictonaries with information of employess.
    #step1 initializing variables
    BAEmp_Names = []
    BA_sales = []
    Sales = []
    #Finding average of the sales
    for emp_info in Employee_data:
        average =sum(sales/len(sales))
    #iteration through emp_data
    for emp_info in Employee_data:
        emp_name = emp_info["emp_name"]
        sales = emp_info ["sales"]
        #checking the employees whose sales are below average
        if sales<average:
            then BA_sales = ['sales']
            BAEmp_Nmaes = ['emp_name'
            #if there are multiple employees add them to the list]
            add emp_name to BAEmp_Names
print ("BAEmp_names")
lower_averageemp(Employee_data)