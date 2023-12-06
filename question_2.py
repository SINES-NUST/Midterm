Assumption: Document is an excel sheet, a CSV file, each column contains: name, sales, amount earned etc. 

1- import pandas as pd
2- reading csv file by providing path to file or calling its name
3- storing the csv file into a dataframe called df 
4- slicing the sales column from datafile abd saving it as a list called employee_sales
5- creating a loop that reads elements 0 - -1 of employee sales 
     count = count+1 
     saves value of count in variable total_num_sales
6- creating a second loop for totalling sales 
    for ith element in employee_sales from 0 - -1 
      sum ith elements and store them in variable called total_sales      
      return total_sales
7- creating a function called avg_sales that takes two functional arguments:
      divides a by b and stores value in variabel c 
        return c
8- calling function avg_sales with arguments total_sales and total_num_sales
9- we get output variable called salesavg 
10- Slicing employee names into another list called employees
11- creating a conditional statement in a loop 
      for emp in employee_sales: 
         if ith element < salesavg
           print("sale below average of", ith element)
           print("employee name is:", ith employee)
           
     
